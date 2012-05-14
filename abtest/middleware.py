from models import Test


class TestMiddleware(object):

    def process_template_response(self, request, response):
        """ Before the template is rendered, check if there is an
        active test on that template name, and if there is, replace
        the template name with an alternative for the current
        session.
        """
        try:
            test = Test.objects.get(template_name=response.template_name[0],
                                    active=True)
        except Test.DoesNotExist:
            return response

        response.context_data['abtest_id'] = test.pk
        alternative = test.get_alternative(request.session)

        if alternative:
            response.template_name = alternative.template_name
            alternative.log_view()

        return response
