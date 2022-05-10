import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
