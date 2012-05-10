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