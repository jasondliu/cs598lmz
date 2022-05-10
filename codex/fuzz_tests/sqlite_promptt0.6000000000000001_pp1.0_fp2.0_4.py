import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
try:
    sqlite3.connect(":memory:")
except sqlite3.OperationalError:
    print("Failed to connect to sqlite3")
    sys.exit(1)

# Test ctypes.util.find_library()
if not ctypes.util.find_library("pthread"):
    print("Failed to find libpthread")
    sys.exit(1)

# Test threading.Lock()
lock = threading.Lock()
lock.acquire(timeout=0.1)
lock.release()

# Test ctypes.CDLL()
ctypes.CDLL(ctypes.util.find_library("pthread"))

# Test ctypes.string_at()
ctypes.string_at(0, 0)

# Test ctypes.memset()
ctypes.memset(0, 0, 0)

# Test ctypes.util.find_library()
if not ctypes.util.find_library("z"):
    print("Failed to find libz")
    sys.exit(1)

#
