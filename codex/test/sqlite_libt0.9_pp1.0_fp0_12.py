import ctypes
import ctypes.util
import threading
import sqlite3
import traceback
import mmap
import os
import contextlib
import Queue
import time
import datetime
import logging
import traceback
import socket, select

log = logging.getLogger(__name__)

logging.basicConfig(format='%(asctime)s [%(process)d %(name)s] %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
log.setLevel(logging.INFO)

#log.setLevel(logging.DEBUG)
#logging.getLogger(__name__).setLevel(logging.DEBUG)

# Protect all writes within the process.
# If you don't call this and your process is multithreaded, you're
# asking for serious problems and/or corrupt data.
# or better yet, use an existing db.
db_lock = threading.Lock()

# Can't use signals because the library is using threading to poll the device.
# So we'll control everything from the main thread instead, polling
