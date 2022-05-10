import ctypes
import ctypes.util
import threading
import sqlite3
import os
import datetime
import logging
import json
import sys
import argparse


# Create logger
logger = logging.getLogger('osx_activity_logger')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


# Get path to the SQLite database for login items
LOGINITEMS_DB_PATH = os.path.expanduser(
    '~/Library/Application Support/com.apple.loginitems/SystemItems.plist')

# Get path to the SQLite database for user activity
ACTIVITY_DB_PATH = os.path.expanduser(
    '~/Library/Application Support/com.apple.loginitems/Activity.db')

# Get path to the SQLite database for user activity
ACTIV
