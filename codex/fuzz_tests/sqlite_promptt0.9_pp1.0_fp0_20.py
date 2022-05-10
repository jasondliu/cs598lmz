import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:") for in-memory db.
# Note for Python 3.8+:
# The test uses sqlite3.sqlite_version_info, which is not available in Python 3.8+.
# It looks like that the ctypes module can't import the sqlite3 library.
# If you installed sqlite3 with 3.7 and upgrade to 3.8, then most likely that is the cause.
# This can happen if you don't uninstall sqlite3 before you upgrade.
# As a result, there's no actual library loaded, so the ctypes.util.find_library("sqlite3") fails and ctypes raises an error.

# For Python 3.8+ the workaround is to set the environment variable "LD_LIBRARY_PATH" to the correct location of the sqlite3 library.
# In Pop!_OS the location is "/usr/lib/x86_64-linux-gnu/libsqlite3.so.0.8.6".
# Check yours by running "$ ldconfig -v 2>/dev/null | grep /libsqlite3.so." (w/o double quotes).
