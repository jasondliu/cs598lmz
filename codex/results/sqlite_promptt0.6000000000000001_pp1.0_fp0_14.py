import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connections.Connection
import _sqlite3

# This test assumes that the system sqlite library has
# been compiled with thread support.  On Debian, you can
# install the libsqlite3-0 package to get such a library.

class TestThreads(unittest.TestCase):
    def setUp(self):
        self.lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
        self.lib.sqlite3_threadsafe.restype = ctypes.c_int

    def test_threadsafe(self):
        self.assertEqual(self.lib.sqlite3_threadsafe(), 1)

    def test_threaded_connections(self):
        # Test that connections can be used from multiple threads
        # without any problems.
        def worker(id):
            try:
                with sqlite3.connect(':memory:') as con:
                    con.execute('select * from sqlite_master')
            except:
                exceptions[id] = sys.exc_info()
        exceptions = {}
        threads = [thread
