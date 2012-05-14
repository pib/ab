This app contains all the logic of the A/B testing framework.

The process of doing an A/B test goes something like this:

0. Enable to ab_test app and middleware in settings.py.

1. Design two (or more) templates you wish to test against a specific
   goal (site registration, for example).

2. Create a test via the admin interface, choose a base template name
   to be the general template name, also include your alternatives
   from step 1.

3. Use the base template name in a view (either a generic view or
   render_to_response call from a function view). The template name
   will be changed to one of the actual alternative template names
   before rendering. Also, an attribute "ab_test_id" will be added to
   the template context, with a value of the ID of the test the base
   template name is associated with.

4. Set up code to call Test.goal(request) when the goal is met (person
   registers). In the example, this works by posting ab_test_id to the
   register view, which then calls Test.goal.

5. Set the test to active, let run for as long as needed to determine
   which version performs better.

6. Once a winner is determined, rename that file to match the base
   template name of the test, and deactivate the test.