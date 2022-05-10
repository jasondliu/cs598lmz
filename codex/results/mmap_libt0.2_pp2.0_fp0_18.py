import mmap
import os
import re
import sys
import time
import traceback

from datetime import datetime
from datetime import timedelta

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import connection
from django.db import transaction

from panda import solr
from panda.models import Dataset
from panda.models import Export
from panda.models import ExportFile
from panda.models import ExportTask
from panda.models import TaskStatus
from panda.tasks import ExportTaskStatusTask
from panda.utils.export import ExportRunner
from panda.utils.export import ExportWriter
from panda.utils.export import UnicodeWriter
from panda.utils.mail import send_mail
from panda.utils.mongo import NoRecordsFound
from panda.utils.mongo import mongo_connect
from panda.utils.mongo import mongo_ensure_indexes

class Command(BaseCommand):
    args = '<export_id>'
    help = 'Export a dataset'

   
