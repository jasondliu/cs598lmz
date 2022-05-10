import weakref

from os.path import join

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.files.storage import default_storage
from django.db import models

from djangobmf.models import Document, Category
from djangobmf.settings import TMP_PATH


class Command(BaseCommand):
    help = 'Import a pdf file for a bmf document'

    def add_arguments(self, parser):
        parser.add_argument('--file', dest='file', default=False, help='The path to the file')
        parser.add_argument('--pk', dest='pk', default=False, help='The pk of the document')
        parser.add_argument('--category', dest='category', default=False, help='The slug of the category')

