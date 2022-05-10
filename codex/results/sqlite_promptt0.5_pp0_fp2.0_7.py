import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
try:
    conn = sqlite3.connect(":memory:")
except:
    print "You need to install sqlite3"
    print "On Ubuntu, try: sudo apt-get install python-sqlite"
    sys.exit(1)

# Test ctypes.util.find_library
libc = ctypes.util.find_library("c")
if not libc:
    print "You need to install libc"
    print "On Ubuntu, try: sudo apt-get install libc6-dev"
    sys.exit(1)

# Test ctypes.CDLL
libc = ctypes.CDLL(libc)
if not libc:
    print "You need to install libc"
    print "On Ubuntu, try: sudo apt-get install libc6-dev"
    sys.exit(1)

# Test libc.pthread_create
libc.pthread_create(None, None, None, None)

# Test libc.pthread_join
libc.pthread_join(None, None)

# Test thread
