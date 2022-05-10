import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# local configs
try:
    from .local import *
except ImportError:
    pass

# now we are on the production server
if ON_PRODUCTION:
    from .production import *
    INSTALLED_APPS += PRODUCTION_INSTALLED_APPS
    ROOT_URLCONF = 'urls.production'
    SITE_ID = 1
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_REGION = os.environ.get('AWS_REGION')

    STATICFILES_STORAGE = 'courses.storage_backends.StaticStorage'
   
