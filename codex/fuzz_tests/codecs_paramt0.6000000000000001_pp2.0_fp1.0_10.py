import codecs
codecs.register_error("strict", codecs.ignore_errors)

# This is a minimal settings file.  It only sets the settings that are
# actually needed to run the tests.  It also sets some that are needed
# for other things in the Django test suite.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

INSTALLED_APPS = [
    'django.contrib.sessions',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'zinnia',
    'zinnia.tests',
]

SITE_ID = 1
SECRET_KEY = 'secret-key'

ROOT_URLCONF = 'zinnia.tests.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
   
