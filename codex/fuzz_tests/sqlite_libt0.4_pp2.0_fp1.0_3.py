import ctypes
import ctypes.util
import threading
import sqlite3
import time
import datetime
import os
import shutil
import sys
import platform
import logging
import logging.handlers

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Log to a file
logfile = logging.handlers.RotatingFileHandler('/var/log/sensord.log', maxBytes=1000000, backupCount=5)
logfile.setLevel(logging.DEBUG)
logfile.setFormatter(formatter)
logger.addHandler(logfile)

# Also log to stdout
stdout = logging.StreamHandler(sys.stdout)
stdout.setLevel(logging.DEBUG)
stdout.setFormatter(formatter)
logger.addHandler(stdout)

# Load the library
lib = ctypes.CDLL(ctypes.util.find_library('sensor'
