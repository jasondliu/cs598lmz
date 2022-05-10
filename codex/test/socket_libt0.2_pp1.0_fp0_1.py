import socket
import sys
import time
import threading
import os
import signal
import random
import string
import json
import re
import traceback
import logging
import logging.handlers
import datetime

from pprint import pprint

from config import *
from utils import *

#
# Global variables
#

#
# Logging
#

logger = logging.getLogger('ircbot')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=LOG_FILE_MAX_SIZE, backupCount=LOG_FILE_BACKUP_COUNT)
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh
