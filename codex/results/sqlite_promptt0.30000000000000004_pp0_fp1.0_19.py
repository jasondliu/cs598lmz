import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# Test sqlite3.connect()

class sqlite3_connect_Test(unittest.TestCase):
    def test_connect_1(self):
        """Test sqlite3.connect()"""
        self.assertRaises(TypeError, sqlite3.connect)
        self.assertRaises(TypeError, sqlite3.connect, 1)
        self.assertRaises(TypeError, sqlite3.connect, "")
        self.assertRaises(TypeError, sqlite3.connect, "", 1)
        self.assertRaises(TypeError, sqlite3.connect, "", "")
        self.assertRaises(TypeError, sqlite3.connect, "", "", 1)
        self.assertRaises(TypeError, sqlite3.connect, "", "", "")
        self.assertRaises(TypeError, sqlite3.connect, "", "", "", 1)
        self.assertRaises(TypeError, sqlite3.connect, "", "", "", "")
        self.assertRaises(TypeError,
