import threading
threading.stack_size(67108864)

from django.conf import settings
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "buddybot.settings")

application = get_wsgi_application()

if settings.DEBUG:
    from django.core.wsgi import get_wsgi_application
    from dj_static import Cling

    application = Cling(get_wsgi_application())

if settings.DEBUG:
    from django.core.wsgi import get_wsgi_application
    from dj_static import Cling

    application = Cling(get_wsgi_application())

call_command('syncdb')
call_command('migrate')

import django
django.setup()

from buddybot import views

import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("
