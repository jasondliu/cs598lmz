import ctypes
import ctypes.util
import threading
import sqlite3
import time
import logging
import logging.handlers
import sys
import os
import glob
import re

#------------------------------------------------------------------------------
# Global Variables
#------------------------------------------------------------------------------

# Database Names
DB_NAME = "./records.db"

# Record Names
MACHINE_RECORD = "machine.db"

# Record Types
MACHINE = "machine"

# Logging Variables
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)
LOG_FILE = "./logs/orion_log.log"
LOG_SIZE = 1048576
LOG_COUNT = 5
LOG_FORMAT = "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"
LOG_DATE_FORMAT = "%m-%d-%y %H:%M:%S"

#------------------------------------------------------------------------------
# Logging Setup
#------------------------------------------------------------------------------

# Logging Setup
log_handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=LOG_SIZE,
