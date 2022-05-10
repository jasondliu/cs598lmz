import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
from sqlite3 import *

# Test the sqlite3.enable_callback_tracebacks() feature
sqlite3.enable_callback_tracebacks(True)

# Test the sqlite3.threadsafety property.
print "sqlite3.threadsafety:", sqlite3.threadsafety

# Test the sqlite3.threadsafety property.
print "sqlite3.paramstyle:", sqlite3.paramstyle

# Test the sqlite3.version property.
print "sqlite3.version:", sqlite3.version

# Test the sqlite3.sqlite_version property.
print "sqlite3.sqlite_version:", sqlite3.sqlite_version

# Test the sqlite3.sqlite_version_info property.
print "sqlite3.sqlite_version_info:", sqlite3.sqlite_version_info

# Test the sqlite3.sqlite_version_info property.
print "sqlite3.sqlite_version_info:", sqlite3.sqlite_version_info

# Test the sqlite3.
