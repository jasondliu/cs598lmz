import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import re
import time
import datetime
import ConfigParser
import traceback
import logging
import logging.handlers

from optparse import OptionParser
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
import urlparse

_logger = None
_db = None
_config = None
_session = None
_session_lock = None
_timer = None
_timer_lock = None

_CONFIG_FILE = 'config.ini'
_DB_FILE = 'db.sqlite'
_LOG_FILE = 'log.txt'

_SESSION_ID = 'session_id'
_SESSION_TIMEOUT = 5*60 # 5 minutes

_SESSION_EXPIRED = -1

_SESSION_STATUS_ACTIVE = 0
_SESSION_STATUS_EXPIRED = 1

_TIMER_STATUS_ACTIVE = 0
_TIMER_STATUS_EXPIRED = 1

_TIMER_ID = 'timer_id'

_LOG_FORM
