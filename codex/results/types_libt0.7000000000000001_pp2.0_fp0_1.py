import types
types.ModuleType = types.ModuleType

from django_firebase_cloud_messaging.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
