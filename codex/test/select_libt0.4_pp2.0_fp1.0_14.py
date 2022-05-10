import select
import sys
import time
import traceback

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import close_old_connections

from . import autoreload
from . import django_autoreload
from . import django_wsgi
from . import runserver_plus
from . import wsgi


class Command(BaseCommand):
    help = "Starts a lightweight Web server for development."

    # Validation is called explicitly each time the server is reloaded.
    requires_system_checks = False
