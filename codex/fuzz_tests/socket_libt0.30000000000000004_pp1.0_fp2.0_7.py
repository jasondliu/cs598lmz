import socket
import time

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from ... import models
from ... import utils

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Runs a local development server for the application'

    def add_arguments(self, parser):
        parser.add_argument(
            '--port',
            dest='port',
            default=settings.DEFAULT_PORT,
            type=int,
            help='Port to run the server on',
        )
        parser.add_argument(
            '--host',
            dest='host',
            default=settings.DEFAULT_HOST,
            type=str,
            help='Host to run the server on',
        )
        parser.add_argument(
            '--no-reload',
            dest='use_reloader',
            action='store_false',
            help='Tells Django to NOT use the auto-reloader',
       
