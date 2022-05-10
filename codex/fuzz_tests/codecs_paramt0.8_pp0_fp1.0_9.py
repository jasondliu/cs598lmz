import codecs
codecs.register_error('surrogate_or_strict', codecs.surrogatepass_or_strict)


def run_tests():
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        INSTALLED_APPS=('django.contrib.auth',
                        'django.contrib.sessions',
                        'django.contrib.contenttypes',
                        'django.contrib.admin',
                        'ccbclib'),
        MIDDLEWARE_CLASSES=(
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
        ),
        LOGGING={
            'version': 1,
            'disable_existing_loggers': True,
            'handlers': {
                'null': {

