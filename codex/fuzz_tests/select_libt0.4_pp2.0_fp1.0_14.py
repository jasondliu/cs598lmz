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

    def add_arguments(self, parser):
        parser.add_argument(
            'addrport', nargs='?',
            help='Optional port number, or ipaddr:port'
        )
        parser.add_argument(
            '--ipv6', '-6', action='store_true', dest='use_ipv6', default=False,
            help='Tells Django to use an IPv6 address.',
        )
        parser.add_argument(
            '--nore
