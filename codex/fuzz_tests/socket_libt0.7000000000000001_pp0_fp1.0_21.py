import socket
import sys
import threading
import time
import traceback
import urllib.request
import urllib.parse

from random import randrange

from app import utils
from app.config import config
from app.config import logging
from app.config import constants
from app.config import exceptions
from app.config.utils import dict_factory
from app.db import api as db_api
from app.tasks import agent_task

CONF = config.CONF
LOG = logging.getLogger(__name__)

_TASK_STATE = ['INSTALLING', 'INSTALLED', 'RUNNING', 'STOPPED',
               'REMOVING', 'REMOVED', 'UNMANAGED']
_CONTAINER_STATE = ['CREATED', 'STARTING', 'STARTED', 'STOPPING',
                    'STOPPED', 'RESTARTING', 'PAUSING', 'PAUSED',
                    'UNPAUSING', 'DELETING', 'DELETED']

_HEALTH_CHECK_INTERVAL = CON
