import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import datetime
import traceback
import subprocess
import logging
import logging.handlers
import configparser

# load configuration
config = configparser.ConfigParser()
config.read('config.ini')

# set up logging
logger = logging.getLogger('vpn-monitor')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.handlers.RotatingFileHandler('vpn-monitor.log', maxBytes=10485760, backupCount=3)
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
