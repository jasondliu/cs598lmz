import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

class TestSqlite3(unittest.TestCase):

    def test_connect(self):
        self.assertRaises(TypeError, sqlite3.connect)
        self.assertRaises(sqlite3.OperationalError,
                          sqlite3.connect, ':memory:', uri=True)
        self.assertRaises(sqlite3.OperationalError,
                          sqlite3.connect, ':memory:', uri=True, check_same_thread=False)
        self.assertRaises(sqlite3.OperationalError,
                          sqlite3.connect, ':memory:', uri=True, check_same_thread=False, isolation_level=None)
        self.assertRaises(sqlite3.OperationalError,
                          sqlite3.connect, ':memory:', uri=True, check_same_thread=False, isolation_level=None, factory=None)
