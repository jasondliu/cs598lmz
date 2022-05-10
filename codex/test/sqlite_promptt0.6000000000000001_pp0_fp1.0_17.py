import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

class testSQLite3(unittest.TestCase):
    def test_connect(self):
        """
            Test sqlite3.connect()
        """
        self.assertRaises(TypeError, sqlite3.connect)
        self.assertRaises(sqlite3.OperationalError, sqlite3.connect, ':memory:')
        self.assertRaises(sqlite3.OperationalError, sqlite3.connect, '')
        self.assertRaises(sqlite3.OperationalError, sqlite3.connect, '.')
        self.assertRaises(sqlite3.OperationalError, sqlite3.connect, '::::')
        self.assertRaises(sqlite3.OperationalError, sqlite3.connect, 'file:')
        self.assertRaises(sqlite3.OperationalError, sqlite3.connect, 'file:test')
        self.assertRaises(sqlite3.OperationalError, sqlite3.connect, 'file::memory:')
