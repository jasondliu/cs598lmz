import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import logging

# Constants

# Default database path
DEFAULT_DB_PATH = 'db/main.db'

# Default table name
DEFAULT_TABLE_NAME = 'main'

# Default table schema
DEFAULT_TABLE_SCHEMA = 'id INTEGER PRIMARY KEY AUTOINCREMENT, time INTEGER, name TEXT, value REAL'

# Default logging level
DEFAULT_LOGGING_LEVEL = logging.INFO

# Default logging format
DEFAULT_LOGGING_FORMAT = '%(asctime)s %(levelname)s %(message)s'

# Default logging date format
DEFAULT_LOGGING_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

# Default logging file
DEFAULT_LOGGING_FILE = 'logs/sensor_log.log'

# Default logging file size
DEFAULT_LOGGING_FILE_SIZE = 1024 * 1024 * 10

# Default logging file count
DEFAULT_
