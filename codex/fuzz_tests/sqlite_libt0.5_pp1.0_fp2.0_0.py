import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import sys
import traceback
import subprocess
import re

# Set up logging
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)

# Load libc
libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)

# Some constants
DB_PATH = '/home/pi/pi-db/pi.db'
PIPE_PATH = '/tmp/pi-pipe'

# Lock to protect the database
db_lock = threading.Lock()

# Some globals
last_update = 0
db_conn = None
db_cur = None
pipe_fd = None

# Set up a pipe for communicating with the Pi
def setup_pipe():
    global pipe_fd

    # Create the pipe
    try:
        os.mkfifo(PIPE_PATH)
    except OSError:
        pass

    # Open the pipe
    pipe_fd = libc.open(PIPE_PATH
