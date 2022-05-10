import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
import time
import os
import re
import sys
import glob
import base64
import hashlib
import datetime
import tempfile
import shutil
import random
import math
import json
import uuid
import urllib.request
import urllib.parse
import urllib.error
import logging
import logging.handlers

# Define the global variables
global database
global cursor
global config
global logger
global logger_handler
global logger_formatter
global hash
global tmp_dir
global tmp_file
global database_connection

# Check if the database file exists
if os.path.isfile("database.db"):
    database_connection = sqlite3.connect('database.db', check_same_thread=False)
else:
    database_connection = sqlite3.connect(':memory:', check_same_thread=False)

# Get the database
database = database_connection.cursor()

# Set the hash
hash = hashlib.sha256()

# Create the logger
logger = logging.getLogger('logger
