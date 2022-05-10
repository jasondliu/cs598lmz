import ctypes
import ctypes.util
import threading
import sqlite3
import signal
import sys
import os
import json
import time
import logging
import logging.handlers
import traceback
import random
import hashlib
import re

# Setup the logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.handlers.SysLogHandler(address='/dev/log')
formatter = logging.Formatter('%(module)s[%(process)d]: %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Setup the database
db = sqlite3.connect('/var/log/pam_smartcard.db', check_same_thread=False)
c = db.cursor()

# Create the tables
