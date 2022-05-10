import mmap
import os
import re
import sys
import time
import traceback

from collections import defaultdict
from datetime import datetime
from itertools import chain
from operator import itemgetter
from optparse import OptionParser
from pprint import pprint
from subprocess import Popen, PIPE

from django.core.management import setup_environ
from django.core.exceptions import ObjectDoesNotExist

from settings import settings
setup_environ(settings)

from django.db import connection, transaction
from django.db.utils import IntegrityError

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from tagging.models import Tag, TaggedItem

from panda.models import Category, Dataset, DataUpload, UserProxy, TaskStatus
from panda.utils.mail import send_mail

# Python 2.5 compatibility
if not hasattr(defaultdict, 'iteritems'):
    def iteritems(d):
        return d.iteritems()
else:
    def iteritems
