import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

try:
    from settings_local import *
except ImportError:
    raise Exception("There is no settings_local.py file. Please create one with your settings.")

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8!d@!(y)5*5$*&o0t8k-t*$&1+-_t0r*r0c%1b+#l@^0!x$*8d'

# SECURITY WARNING: don't run with debug turned
