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

class TestCtypesFunc(unittest.TestCase):
    def setUp(self):
        self.lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

    def test_sqlite3_create_function(self):
        self.assertRaises(sqlite3.OperationalError, self.lib.sqlite3_create_function, 0, b"test", 1, None, None, None)
        self.lib.sqlite3_open(DB_URI.encode("utf-8"), ctypes.byref(ctypes.c_void_p()))
        self.lib.sqlite3_create_function(ctypes.c_void_p(), b"test", 1, None, None, None)

    def test_sqlite3_create_function_with_python_func(self):
        db = sqlite3.connect(DB_URI, uri=True)

        def test_fn(a, b):
            return a

        db.create_function("test", 2, test_fn)

        self.
