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

c_cb = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)

encoder = ctypes.CDLL(ctypes.util.find_library("sqlite3"), mode=ctypes.RTLD_GLOBAL)
decoder = ctypes.CDLL(ctypes.util.find_library("sqlite3"), mode=ctypes.RTLD_GLOBAL)

encoder._Z14sqlite3_value8_callbackP11sqlite3_valuePv = c_cb
decoder._Z14sqlite3_value8_callbackP11sqlite3_valuePv = c_cb

class TestCase(unittest.TestCase):
    def setUp(self):
        self.db_con = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

        def test_fn(a, b):
            return a

        self.db_con.create_function("test", 2, test_fn)
