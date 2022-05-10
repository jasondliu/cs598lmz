import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import datetime
import re
import urllib
import urllib2
import json
import logging
import logging.handlers
import traceback

#
# Global variables
#

# Database
db = None

# Logging
logger = None

# Configuration
config = None

#
# Functions
#

def init():
    global config, db, logger

    # Load configuration
    config = Config()
    config.load()

    # Initialize database
    db = Database()
    db.init()

    # Initialize logger
    logger = Logger()
    logger.init()

def cleanup():
    global db, logger

    # Cleanup logger
    logger.cleanup()

    # Cleanup database
    db.cleanup()

def run():
    global config, db, logger

    # Initialize
    init()

    # Main loop
    while True:
        try:
            # Check if we should exit
            if config.get('exit'):
                break

            # Check if we should reload
