import codecs
codecs.register_error('strict', codecs.ignore_errors)

AUTHOR = u'Sebastian L\xf6tters'
SITENAME = u'Sebastian L\xf6tters'
SITEURL = 'http://sebastian-loetters.de'
#SITEURL = 'http://localhost:8000'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
#DISPLAY_PAGES_ON_MENU = False

THEM
