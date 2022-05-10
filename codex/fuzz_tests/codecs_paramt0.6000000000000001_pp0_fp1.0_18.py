import codecs
codecs.register_error('strict', codecs.ignore_errors)

from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from django.db import transaction
from django.contrib.auth.models import User

from core.models import *
from core.utils import *

class Command(BaseCommand):
    help = 'Import data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)
        parser.add_argument('--skip-first-line', action='store_true', default=False)
        parser.add_argument('--verbose', action='store_true', default=False)
        parser.add_argument('--commit', action='store_true', default=False)
        parser.add_argument('--dry-run', action='store_true', default=False)

    def handle(self, *args, **options):
        filename = options['filename']
        skip_first_line = options['skip_first_line']
        verbose = options['verb
