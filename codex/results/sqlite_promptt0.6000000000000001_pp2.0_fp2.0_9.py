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

def check_sqlite_version(conn, minversion):
    # Checks that the sqlite version used to build pysqlite satisfies
    # minversion.  minversion is a sequence of three ints, as in
    # (3, 3, 8).
    #
    # The pysqlite version used in Python 2.5 is based on sqlite 3.3.8.
    #
    # This test currently checks for a minimum version of 3.3.8, but
    # that may change if a later version of sqlite is incorporated.
    #
    #
