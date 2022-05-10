import ctypes
import ctypes.util
import threading
import sqlite3
import traceback
import json
import time
import sys
import signal
import os
import argparse

import logging
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='Runs the background service for the gateway')
parser.add_argument('--debug', action='store_true', help='show debug output')
args = parser.parse_args()

if args.debug:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

logger.info("Starting")

# Load the configuration from the database
config_db = sqlite3.connect("/home/pi/gateway-server/config.db")
config_cursor = config_db.cursor()
config_cursor.execute("SELECT name, value FROM config")
config = {}
for row in config_cursor:
    config[row[0]] = row[1]
config_db.close()
logger.info("Configuration loaded: {}".format(config))

# Load
