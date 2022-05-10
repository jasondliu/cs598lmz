import ctypes
import ctypes.util
import threading
import sqlite3
import subprocess
import os
import time
import sys
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

# Check if the user is root
if os.geteuid() != 0:
    sys.exit('You need to run this script as root!')

# Check if the user has a valid config file
if not os.path.isfile('/etc/sigterm.conf'):
    sys.exit('You need to create a valid config file!')

# Read config file
config = {}
with open('/etc/sigterm.conf') as f:
    for line in f:
        if not line.startswith('#'):
            (key, val) = line.split(':')
            config[key] = val.strip()

# Check if the user has a valid database file
