import mmap
import os
import sys
import time
from time import sleep

from django.core.management.base import BaseCommand
from django.db import connection
from django.db.models import F

from apps.core.models import (
    Comment,
    CommentVote,
    Post,
    PostVote,
    User,
)
from apps.core.utils import get_client_ip
from apps.core.utils.ip import get_ip_country_code


class Command(BaseCommand):
    help = 'Loads data from the given file'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            default='data/data.csv',
            help='Data file to load.'
        )

    def handle(self, *args, **options):
        self.stdout.write('Loading data from %s' % options['file'])
        self.load_data(options['file'])

    def load_data(self, file_name):
        with open(file_name, '
