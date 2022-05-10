import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)
import os
import sys
import time
import unittest
import weakref

from test import support

# Skip test if _sqlite3 module not present.
support.import_module('_sqlite3')

# For the special purpose of testing pysqlite, we need to be able to
# load the sqlite library from a specific path.
# We do this by using ctypes.util.find_library to find the library
# and then load it manually.
sqlite_lib = ctypes.util.find_library("sqlite3")
if not sqlite_lib:
    raise unittest.SkipTest("sqlite library not found")
sqlite = ctypes.CDLL(sqlite_lib)

# Test that the sqlite library we loaded is recent enough.
