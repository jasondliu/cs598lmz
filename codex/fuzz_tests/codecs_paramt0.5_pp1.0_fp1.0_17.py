import codecs
codecs.register_error('strict', codecs.ignore_errors)

from django.core.management.base import BaseCommand
from django.conf import settings

from ...models import *
from ...utils import *

class Command(BaseCommand):
    help = 'Import a dictionary of words from a text file'

    def add_arguments(self, parser):
        parser.add_argument('--filename', '-f', type=str,
            help='Filename to import')

    def handle(self, *args, **options):
        filename = options['filename']
        if not filename:
            print("You must specify a filename")
            return

        # Do the actual import
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                word = line.strip().lower()
                Word.objects.get_or_create(text=word)
