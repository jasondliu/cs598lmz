import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(). For this to work, the sqlite3.dll has to be in the
# PATH, or the .dll.a, .dll.so or .dll.dylib has to be in the same directory as
# this file.
sqlite3.connect(':memory:').close()

libc = ctypes.CDLL(ctypes.util.find_library('c'))

# Test whether the system has clock_getres.  If so, we can implement
# time.clock_getres().
try:
    libc.clock_getres
except AttributeError:
    has_clock_getres = False
else:
    has_clock_getres = True

# Test whether the system has clock_gettime.  If so, we can implement
# time.clock_gettime().
try:
    libc.clock_gettime
except AttributeError:
    has_clock_gettime = False
else:
    has_clock_gettime = True

# Test whether the system has clock_settime.  If so, we can implement
# time.clock_settime().
