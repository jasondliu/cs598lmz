import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import datetime
import logging
import logging.handlers
import subprocess
import re
import signal
import socket
import struct
import fcntl
import errno
import traceback

# Constants

# The default location of the database file
DEFAULT_DB_FILE = '/var/lib/bluetooth/%s/%s'

# The default value for the --db option
DEFAULT_DB = DEFAULT_DB_FILE % (os.uname()[1], 'linkkeys')

# The default location of the pid file
DEFAULT_PID_FILE = '/var/run/bluetooth/%s.pid'

# The default value for the --pid option
DEFAULT_PID = DEFAULT_PID_FILE % os.uname()[1]

# The default location of the log file
DEFAULT_LOG_FILE = '/var/log/bluetooth/%s.log'

# The default value for the --log option
DEFAULT_LOG = DEFAULT_LOG_FILE % os.uname()
