import ctypes
import ctypes.util
import threading
import sqlite3
import time
import copy
import socket
import logging
import logging.handlers
import logging.config
import datetime
import traceback
import urllib.request
import urllib.parse
import urllib.error
import json
import os
import sys
import csv
import re
import pytz
import dateutil.parser
import requests

#------------------------------------------------------------------------------
# Globals

# Name of this application
APP_NAME = "sjs-logger"

# Version number
APP_VERSION = "1.0.0"

# The name of this file
APP_FILE = os.path.basename(__file__)

# The location of the config file
CONFIG_FILE = APP_NAME + ".conf"

# The location of the log file
LOG_FILE = APP_NAME + ".log"

# The location of the pid file
PID_FILE = APP_NAME + ".pid"

# The location of the database file
DB_FILE = APP_NAME + ".db"

# The location of the data file
DATA_FILE = APP_NAME + ".
