import mmap
import os
import re
import sys
import time

from collections import defaultdict
from datetime import datetime
from optparse import OptionParser
from subprocess import Popen, PIPE

from pyinotify import WatchManager, Notifier, ProcessEvent, IN_DELETE, IN_CREATE, IN_MODIFY

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.timezone import utc

from panda.models import Dataset, DataUpload
from panda.utils.mail import send_mail

class Command(BaseCommand):
    """
    Monitor a directory for new files and upload them to datasets.
    """
    option_list = BaseCommand.option_list + (
        make_option('-d', '--directory',
            action='store',
            dest='directory',
            default=None,
            help='Directory to monitor for new files.'),
        make_option('-e', '--extension',
            action='store',
            dest='ext
