import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse

from datetime import datetime
from optparse import OptionParser
from subprocess import Popen, PIPE

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.models import Q

from panda.models import Dataset, Export, ExportFile
from panda.tasks import ExportFileTask
from panda.utils.mail import send_mail

class Command(BaseCommand):
    help = 'Export data'
    args = '<dataset_slug> <export_id> <export_type> <export_format>'

    def handle(self, *args, **options):
        if len(args) != 4:
            print 'Invalid arguments'
            sys.exit(1)

        dataset_slug, export_id, export_type, export_format = args

        try:
            export = Export.objects.get(id=
