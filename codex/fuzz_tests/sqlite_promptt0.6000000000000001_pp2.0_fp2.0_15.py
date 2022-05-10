import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() was successful
import sys
import os

# Test sqlite3.connect() was successful
try:
    import sqlite3
except ImportError:
    print "Failed to import sqlite3"
    sys.exit(1)


class TestPySQLite3Properties(unittest.TestCase):
    def test_version(self):
        self.assertTrue(isinstance(sqlite3.version, str))
        self.assertTrue(sqlite3.version.count(".") == 2)

    def test_sqlite_version(self):
        self.assertTrue(isinstance(sqlite3.sqlite_version, str))
        self.assertTrue(sqlite3.sqlite_version.count(".") == 2)

    def test_threadsafety(self):
        self.assertTrue(isinstance(sqlite3.threadsafety, int))
        self.assertTrue(sqlite3.threadsafety in (0, 1, 2))

    def test_paramstyle(self):
        self.assertTrue(isinstance(sqlite3.paramstyle, str))
       
