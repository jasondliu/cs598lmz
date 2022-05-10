import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

print(os.environ.get('DJANGO_SETTINGS_MODULE'))
django.setup()

from django.db import connection


KAMAILIO_DB = os.environ['KAMAILIO_DB']
KAMAILIO_HOST = os.environ['KAMAILIO_HOST']
KAMAILIO_PORT = os.environ['KAMAILIO_PORT']
KAMAILIO_USERNAME = os.environ['KAMAILIO_USERNAME']
KAMAILIO_PASSWORD = os.environ['KAMAILIO_PASSWORD']

AUTH_DB = os.environ['AUTH_DB']
AUTH_HOST = os.environ['AUTH_HOST']
AUTH_PORT = os.environ['AUTH_PORT']
AUTH_USERNAME = os.environ['AUTH_USERNAME']
AUTH_PASSWORD = os.environ
