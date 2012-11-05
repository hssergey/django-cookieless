##### django-cookieless ##### 

# Rewrite URLs to add session id for no_cookies decorated views 
# (if False then all page navigation must be via form posts)
COOKIELESS_USE_GET = True

# Rewriting the response automatically rather than use manual <% session_token %> <% session_url %> 
COOKIELESS_REWRITE = False

# NB: Need to add django.core.context_processors.request if using manual tags
# so its available for templatetags/cookieless
if not COOKIELESS_REWRITE:
    import django.conf.global_settings as DEFAULT_SETTINGS
    TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + ('django.core.context_processors.request', )

# Use client ip and browser to encode session key, to add some CSRF protection without being able to use cookies.
COOKIELESS_CLIENT_ID = True

# If this list is populated then only hosts that are specifically whitelisted#  are allowed to post to the server. So any domains that the site is served # over should be added to the list. This helps protect against XSS attacks.
COOKIELESS_HOSTS = ['localhost', ]

#############################

# Settings to be used when running unit tests
# python manage.py test --settings=django-cookieless.test_settings django-cookieless

DATABASE_ENGINE = ''           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = ''             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

INSTALLED_APPS = (
    # Put any other apps that your app depends on here
    'cookieless',
)
SITE_ID = 1

# This merely needs to be present - as long as your test case specifies a
# urls attribute, it does not need to be populated.
ROOT_URLCONF = ''