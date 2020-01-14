**Don't use this as-is. It's way out of date and was just done as a quick proof-of-concept.**

A simple Django app to A/B test alternative registration forms.


Setup
=====

It is assumed that this will be worked on/run inside a virtualenv.

    $ mkvirtualenv ab  # if using virtualenvwrapper

OR

    $ virtualenv ~/.virtualenvs/ab  # if using virtualenv by itself
    $ ~/.virtualenvs/ab/bin/activate

After the virtualenv has been activated, the dependencies can be installed.

    $ pip install -r requirements.txt

Then the DB can be initialized and the site run.

    $ python manage.py syncdb     # setup DB
    $ python manage.py runserver  # run development server

The "syncdb" command will ask if you want to add a superuser. Go ahead
and do so, so you will have access to the admin interface. It will
also load in an initial registration form test, which will be loaded
by the home page of the example site.

Clearing cookies, opening an "incognito mode" window, or running more
than one browser are all acceptable ways to test the random
alternative selection.

Visit the main page several times with several different sessions, and
register a few times as well (the registration form doesn't actually
DO anything but log that a registration happened, it's just there as
an example of how templates can be swapped out with this system).

Now, log in as that same admin use created before, click the Admin
link at the top-right of the page, then from the admin site, click
"Tests". The test should be there, with numbers showing how many views
each of the options got, and what percentage of those views led to
registrations.


Approach
========

A/B testing implementation
--------------------------

My first thought was to see what existing A/B testing frameworks there
are for Django. There are several, but most of them seemed to be
overkill for this specific assignment, so I went with a simple
from-scratch implementation. In a real-life work situation I would
have discussed the options with other developers as well as any
potential users of the feature to determine more specifically what
they need before making the decision.

This A/B testing implementation is done with a custom Django
middleware which selects an alternative template on a per-session
basis, remembering the selection in the user's session. The template
replacement is done via the process_template_response middleware
method, which allows for simply setting a different template name to
be used before the template is rendered.

At the moment, there is one view logged per time one registration form
is viewed, even if that same user has viewed it before (though they
will see the same form each time, as long as they have the same
session). It might make sense to modify this behavior to only logging
one "view" per user, to change the metric from "number of times
registration happened after someone viewed this form" to "number of
people who saw this form who registered".

When registration is completed, a "goal reached" is logged. The
generic name is used since there's nothing really restricting this app
to only working for registration form comparisons. In its current
form, it would work just as well for any page where the user can POST
a form. It would be fairly easy to allow for even more generic goals,
such as simply visiting a certain page, though that would require some
more information to be stored in the Test model.

Visual Design
-------------

Visual design is not my strong suit, so I opted to start with a clean
base via Twitter's [Bootstrap][] framework, on top of which I can
build clean HTML and CSS.


[Bootstrap]: http://twitter.github.com/bootstrap/
