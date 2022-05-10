import ctypes
import ctypes.util
import threading
import sqlite3

my_threading_local = threading.local()

class deleting_conn(sqlite3.Connection):
    def __del__(self):
        self.close()

DB_URI = "file:test?mode=memory"

def my_cb(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    return 1

def my_cb2(p):
    del my_threading_local.a
    return 1

class MyTestCase(unittest.TestCase):
    def test_callback(self):
        # Load SQLite
        sqlite_lib_path = ctypes.util.find_library("sqlite3")
        sqlite_lib = ctypes.CDLL(sqlite_lib_path)

        # Set up callback
        self.assertEqual(1, sqlite_lib.sqlite3_config(ctypes.c_int(45), my_cb, None))
        self.assertEqual(1, sqlite_lib.sqlite3_config(ctypes.c_int(46), my_cb2, None))

        # Create a connection
        conn = sqlite3.connect(DB_URI, uri=True)
        conn.close()

        # Check that callback was fired
        self.assertTrue(hasattr(my_threading_local, "a"))
        del my_threading_local.a

        # Check that callback was fired
       
