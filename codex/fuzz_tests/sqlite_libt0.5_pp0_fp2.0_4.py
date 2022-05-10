import ctypes
import ctypes.util
import threading
import sqlite3
import time
import datetime
import sys
import os
import socket

#------------------------------------------------------------------------------
#
# GLOBALS
#
#------------------------------------------------------------------------------

# The serial port to use for the connection.
SERIAL_PORT = '/dev/ttyUSB0'

# The path to the sqlite3 database.
DB_PATH = '/var/www/html/powermon/powermon.db'

# The name of the table to use in the database.
DB_TABLE = 'powermon'

# The log file to use for the daemon.
LOG_FILE = '/var/log/powermon.log'

# The number of seconds to sleep between readings.
SLEEP_TIME = 10

# The number of readings to take before inserting into the database.
READINGS_PER_INSERT = 100

# The number of readings to take before updating the database.
READINGS_PER_UPDATE = 100

# The number of readings to take before dumping the database.
READINGS_PER_DUMP = 100

# The number of readings to take before checking for a database change.
READINGS_PER_
