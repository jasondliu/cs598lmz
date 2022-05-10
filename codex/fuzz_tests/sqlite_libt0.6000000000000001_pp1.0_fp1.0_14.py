import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import sys
import errno
import re
import ConfigParser
import json
import hashlib
import shutil
import logging
import traceback
import Queue

# Global variables
config_file = "config.ini"
lock_file = "lock.pid"

# Constants
DB_FILE = 'database.sqlite'

# Globals
db_lock = threading.RLock()
db_queue = Queue.Queue()

# Read config file
if not os.path.isfile(config_file):
    print "Error: Config file not found.\n"
    sys.exit(1)

config = ConfigParser.ConfigParser()
config.read(config_file)

if not config.has_option('General', 'log_file'):
    print "Error: Log file not set in config file.\n"
    sys.exit(1)

logfile = config.get('General', 'log_file')

# Logging
logger = logging.getLogger(__name__)
logger.setLevel(
