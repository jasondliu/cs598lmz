import ctypes
import ctypes.util
import threading
import sqlite3
import logging
import logging.handlers
import sys
import os
import time
import re

# Local imports
import config
import utils

# Set up logging
logger = logging.getLogger("main")
logger.setLevel(logging.DEBUG)

# Set up logging to console
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)
console_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

# Set up logging to file
file_handler = logging.handlers.RotatingFileHandler(config.LOG_FILE, maxBytes=config.LOG_SIZE, backupCount=config.LOG_ROTATIONS)
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.
