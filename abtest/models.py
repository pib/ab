from django.db import models


class Test(models.Model):
    """ A model to represent a single A/B test, either in progress
    (active=True) or completed (active=False).

    Technically, they are A/B/N tests, because they may have more than
    one alternative.
    """
    active = models.BooleanField(default=False, db_index=True,
                                 help_text='Is this test currently running?')
    template_name = models.CharField(max_length=128, db_index=True)

    def __unicode__(self):
        return '%s - %s' % (
            self.template_name,
            u' vs. '.join(a.template_name for a in self.alternatives.all()))

    def get_alternative(self, session):
        """ Return a random alternative and store the selection in the
        current session, or return None if there are no alternatives
        associated with this test.
        """
        key = 'abtest_alternative:%s' % self.pk

        try:
            return Alternative.objects.get(pk=session[key])
        except KeyError:
            try:
                alternative = self.alternatives.order_by('?')[0]
                session[key] = alternative.pk
                return alternative
            except IndexError:
                return None


class Alternative(models.Model):
    """ A model to represent one alternative of a specific A/B test.

    Contains a field with the name of the template to use when this
    alternative is chosen.
    """
    test = models.ForeignKey(Test, related_name='alternatives')
    template_name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.template_name

    def log_view(self):
        LogEntry.objects.create(action='V', alternative=self)

    def log_goal_reached(self):
        LogEntry.objects.create(action='G', alternative=self)


class LogEntry(models.Model):
    """ Model to log actions related to the alternatives of an A/B
    test. Used to record each view of a each alternative, as well as
    each time a goal (e.g. registration) is reached after viewing an
    alternative.
    """
    ACTION_CHOICES = (
        ('V', 'View'),
        ('G', 'Goal Reached'),
    )
    action = models.CharField(max_length=1, choices=ACTION_CHOICES, db_index=True)
    alternative = models.ForeignKey(Alternative, related_name='log_entries')
    logged_at = models.DateTimeField(auto_now_add=True)
