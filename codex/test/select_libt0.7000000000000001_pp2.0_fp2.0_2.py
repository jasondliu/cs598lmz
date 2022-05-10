import select
import time
import sys
import threading
import Queue
import json

import networkx as nx

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail

from openipam.hosts.models import *
from openipam.hosts.functions import *

import logging
logger = logging.getLogger('console')

# Setup the django environment
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'openipam.settings'
django.setup()

# Add the django project path
sys.path.append(settings.BASE_DIR)

# Setup the logging
import logging.config
logging.config.dictConfig(settings.LOGGING)


class Hosts(object):
	"""
	Class to manage DHCP hosts.
	"""
