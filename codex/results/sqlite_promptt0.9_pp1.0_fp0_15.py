import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
import os
import sys
# On Python 2.7.9, need to set ssl._create_default_https_context = ssl._create_unverified_context
import ssl

from cozify import cloud
from cozify import config as cozifyconfig
from cozify import hub
from cozify import radio
from cozify import util

from config import config

from hubbackup_util import util as hubbackuputil

from logging import handlers

LOGGER = logging.getLogger(__name__)
if not len(LOGGER.handlers):
    LOGGER.setLevel(config.get('loglevel', 'INFO'))
    logHandler = handlers.TimedRotatingFileHandler(config.get('logfile', 'hubbackup.log'), when='d', interval=1, backupCount=7)
    logFormat = '%(asctime)s %(levelname)s %(message)s'
    logFormatter = logging.Formatter(logFormat)
    logHandler.setFormatter(logFormatter)
