import ctypes
import ctypes.util
import threading
import sqlite3
import datetime
import socket
import subprocess
import sys
import os
import errno
import stat
import logging
import logging.handlers
import time
import copy
import getopt
import fcntl

# constants
_default_pidfile="/var/run/%s.pid"
_default_logfile="/var/log/%s.log"

_default_pidfile=_default_pidfile % os.path.basename(sys.argv[0])
_default_logfile=_default_logfile % os.path.basename(sys.argv[0])

_default_pidfile=os.path.abspath(_default_pidfile)
_default_logfile=os.path.abspath(_default_logfile)

# logging levels
_LOG_DEBUG=logging.DEBUG
_LOG_INFO=logging.INFO
_LOG_WARNING=logging.WARNING
_LOG_ERROR=logging.ERROR
_LOG_CRITICAL=logging.CRITICAL

# log format
_log_format="%(asct
