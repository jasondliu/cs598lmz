import mmap
import os
import sys
import time
import traceback

from datetime import datetime, timedelta
from email import message_from_string
from email.utils import parsedate_tz, mktime_tz
from io import StringIO
from optparse import OptionParser
from threading import Thread

from django.conf import settings
from django.core.mail import mail_admins
from django.utils import timezone

from panda import solr, utils
from panda.models import Dataset, Export, ExportFile, RelatedUpload
from panda.tasks import ExportFileTask, NotifyTask, ProcessUploadTask, UpdateDatasetTask

# Setup Django environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'panda.settings'

def parse_options():
    """
    Parse command line options.
    """
    parser = OptionParser()
    parser.add_option('-s', '--socket', dest='socket',
        help='Path to ZMQ socket')
    parser.add_option('-l', '--log', dest
