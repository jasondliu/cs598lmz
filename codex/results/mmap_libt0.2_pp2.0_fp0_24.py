import mmap
import os
import re
import sys
import time
import traceback

from collections import defaultdict
from datetime import datetime
from optparse import OptionParser
from subprocess import Popen, PIPE

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

from panda import solr, utils
from panda.models import Category, Dataset, DataUpload, TaskStatus
from panda.tasks import ImportTask, NotifyTask, UpdateSearchIndexTask
from panda.utils.mail import send_mail

class Command(BaseCommand):
    args = ''
    help = 'Import data from a file'

    def handle(self, *args, **options):
        parser = OptionParser()
        parser.add_option('-f', '--file', dest='file', help='File to import')
        parser.add_option('-d', '--data-upload', dest='data_upload', help='Data upload to import')
        parser.add_option('-c', '--category', dest='category
