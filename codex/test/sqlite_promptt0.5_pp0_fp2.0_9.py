import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect

libsqlite = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

def test_connect_fail(self):
    with self.assertRaises(sqlite3.OperationalError) as cm:
        sqlite3.connect(':memory:', uri=True)
    self.assertEqual(cm.exception.args[0], 'invalid URI')

def test_connect_fail_thread(self):
    with self.assertRaises(sqlite3.OperationalError) as cm:
        def target():
            sqlite3.connect(':memory:', uri=True)
        t = threading.Thread(target=target)
        t.start()
        t.join()
    self.assertEqual(cm.exception.args[0], 'invalid URI')

