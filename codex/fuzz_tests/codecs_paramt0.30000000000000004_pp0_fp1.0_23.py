import codecs
codecs.register_error('strict', codecs.ignore_errors)

import sys
import os
import re
import time
import datetime
import json
import urllib
import urllib2
import logging
import logging.config
import traceback
from optparse import OptionParser

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

from panda.models import Dataset, TaskStatus
from panda.tasks import ExportTask, ImportTask, NotifyTask, DeleteDatasetTask, DeleteDataUploadTask, DeleteDataFileTask, DeleteUserTask
from panda.utils.mail import send_mail
from panda.utils.notifications import notify

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Monitor and run tasks'
    option_list = BaseCommand.option_list + (
        make_option('-l', '--log-level',
            action='store',
            dest='log_level',
            default='INFO',
            help='Log level'),
       
