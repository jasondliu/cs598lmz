import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# check if sqlite3 is loadable
if ctypes.util.find_library('sqlite3') is None:
    raise RuntimeError('sqlite3 not found')

# check if version is 3.0.0 or newer
sqlite3_version = sqlite3.version
sqlite3_version_tuple = tuple(map(int, sqlite3_version.split('.')))
if sqlite3_version_tuple < (3, 0, 0):
    raise RuntimeError('sqlite3 version is too old')

# check if sqlite3 is thread-safe
sqlite3_threadsafe = sqlite3.threadsafety
if sqlite3_threadsafe == 0:
    raise RuntimeError('sqlite3 is not thread-safe')

# check if sqlite3 is compiled with mutexes enabled
# http://www.sqlite.org/threadsafe.html
sqlite3_dll = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
sqlite3_mutex_status = ctypes.c_int()
sqlite
