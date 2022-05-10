import socket

from requests.exceptions import ConnectionError

from django.core.management.base import BaseCommand
from django.utils import timezone

from lib.calibre.calibreopds import update_feeds
from lib.calibre.utils import CalibreLibrary
from lib.ebooks.models import Category


class Command(BaseCommand):
    help = 'Synchronizes Calibre library with Django database.'

    def add_arguments(self, parser):
        parser.add_argument('--verbose', action='store_true')

    def handle(self, *args, **options):
        verbose = options['verbose']
