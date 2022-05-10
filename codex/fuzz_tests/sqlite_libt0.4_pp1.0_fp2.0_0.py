import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os
import re
import json
import urllib2
import urllib
import traceback
import logging
import logging.handlers
import signal

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.handlers.RotatingFileHandler('/var/log/vpn_monitor.log', maxBytes=1024*1024*10, backupCount=5)
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)
logger.add
