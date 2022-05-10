import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import sys
import errno
import re
import ConfigParser
import json
import hashlib
import shutil
import logging
import traceback
import Queue

# Global variables
config_file = "config.ini"
lock_file = "lock.pid"

# Constants
DB_FILE = 'database.sqlite'

# Globals
db_lock = threading.RLock()
db_queue = Queue.Queue()

# Read config file
