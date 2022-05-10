import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
import os.path
import os
import json
import time
import sys
import re
import string
import struct
import binascii
import logging
import logging.handlers
import subprocess
import traceback

###############################################################################
# Global variables
###############################################################################

# Logging
logger = logging.getLogger('radiologger')
logger.setLevel(logging.DEBUG)
log_file = '/tmp/radiologger.log'
handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=1048576, backupCount=5)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# OOK library
radiologger_path = os.path.dirname(os.path.realpath(__file__))
