import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')
import sys
import os
import time
import tempfile
import unittest
import warnings
from test import support

# Skip test if _sqlite3 module not available.
support.import_module('_sqlite3')

# For the special thread check in test_threadsafety
try:
    import _thread
except ImportError:
    import _dummy_thread as _thread

# Some constants for the test suite
IS_64BIT = (ctypes.sizeof(ctypes.c_voidp) == 8)

# Check if pysqlite was compiled with 2.6 sqlite or not
try:
    sqlite_version_info = sqlite3.sqlite_version_info
except AttributeError:
    sqlite_version_info = (3, 3, 8)

# Check if pysqlite was compiled with 2.5 sqlite or not
try:
    sqlite_version_info25 = sqlite3.sqlite_version_info25
except AttributeError:
    sqlite_version_info25 = (
