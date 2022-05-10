import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
from datetime import datetime
import logging
from logging.handlers import TimedRotatingFileHandler

# Import the shared library
#lib = ctypes.CDLL("lib/liblsm303dlhc.so")
lib = ctypes.CDLL(ctypes.util.find_library("lsm303dlhc"))

# Set up logging
logger = logging.getLogger("lsm303dlhc")
logger.setLevel(logging.DEBUG)
handler = TimedRotatingFileHandler("/var/log/lsm303dlhc.log", when="midnight", interval=1)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

# Define some constants
LSM303DLHC_ACC_ADDRESS = 0x19
