# cmsplugin-auth-content-example

Example django-cms plugin to follow along with the blog post at:
https://www.chicagodjango.com/blog/django-cms-plugin-authenticated-user-variations/


Quickstart
----------

Install:

    pip install -e git+https://github.com/ImaginaryLandscape/cmsplugin-auth-content-example.git#egg=cmsplugin-auth-content


Add ``cmsplugin_auth_content`` to INSTALLED_APPS:

    INSTALLED_APPS = [
        ...
        'cmsplugin_auth_content',
        ...
    ]

Migrate:

    $ python manage.py migrate
