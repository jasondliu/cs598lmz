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

def my_cb_close(p):
    my_threading_local.a.close()
    my_threading_local.a = None
    return 1

def my_cb_init(p):
    my_threading_local.a = None
    return 1

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
        self.lib.sqlite3_open(DB_URI.encode("utf-8"), ctypes.byref(self.conn))
        self.lib.sqlite3_create_function(self.conn, b"test", 2, 0, None, my_cb, None, None)
        self.lib.sqlite3_create_function(self.conn, b"test_close", 0, 0, None, my_cb_close, None, None)
        self.lib.sqlite3_create_function(self.conn, b"test_init", 0, 0, None, my_
