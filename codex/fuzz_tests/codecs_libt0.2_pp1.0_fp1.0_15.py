import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

#
#   Import Django project settings
#
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

#
#   Import and configure the Django application instance
#
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
