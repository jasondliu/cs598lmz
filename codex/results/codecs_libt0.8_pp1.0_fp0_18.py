import codecs
codecs.register_error('replace_spaces', codecs.replace_errors(u' '))

#/usr/local/bin/python2.7 /var/www/DjangoProjects/mysite/manage.py runserver
#/home/kirill/web/env/bin/python3 ~/web/ask/manage.py runserver &

LANGUAGES = {
    'default': {
        'bidi': False,
        'format_numeric': 'n',
        'format_decimal': '.',
        'format_thousands': ',',
        'decimal_symbol': '.',
        'thousands_sep': ','
    }
}

try:
    from .local_settings import *
except ImportError:
    pass

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for
