import ctypes
import ctypes.util
import threading
import sqlite3
import random
import time
import os
import sys
import subprocess
import re

# These are global variables that are used to store the database connection,
# the current database cursor and the current database path
db_conn = None
db_cur = None
db_path = None

# This is the path to the database file.
db_file = "./db/gps.db"

# This is the path to the gpsd daemon.
gpsd_path = "/usr/sbin/gpsd"

# This is the path to the gpsd control socket.
gpsd_socket = "/var/run/gpsd.sock"

# This is the path to the gpsd configuration file.
gpsd_config = "/etc/default/gpsd"

# This is the path to the gpsd log file.
gpsd_log = "/var/log/gpsd.log"

# This is the path to the gpsd pid file.
gpsd_pid = "/var/run/gpsd.pid"

#
