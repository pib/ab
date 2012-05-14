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

Visual Design
-------------

Visual design is not my strong suit, so I opted to start with a clean
base via Twitter's [Bootstrap][] framework, on top of which I can
build clean HTML and CSS.


[Bootstrap]: http://twitter.github.com/bootstrap/