import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
