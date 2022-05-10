import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connections
from sqlite3 import connections
import weakref
from test import support
from test.support import os_helper

# Skip these tests if the _sqlite module wasn't built or the _sqlite3
# module is available.
support.import_module('_sqlite3')
support.import_module('_sqlite3', deprecated=True)

try:
    connections.enable_callback_tracebacks(True)
except Exception:
    pass

# Test the sqlite shell included with pysqlite.

