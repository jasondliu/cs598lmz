import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.settings")

application = get_wsgi_application()

from django.core.cache import cache
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError

from django.conf import settings

from main.models import *

from main.utils import *

from main.cron import *

from django.db import transaction

from datetime import datetime
import time

from django.db import transaction

from django.db.models import
