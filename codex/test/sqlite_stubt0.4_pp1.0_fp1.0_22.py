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
    a = my_threading_local.a
    a.execute("select test(1, 2)")
    return 1

def my_cb3(p):
    a = my_threading_local.a
    a.execute("select test(1, 2)")
    return 1

class TestCase(unittest.TestCase):
    def test_threading(self):
        sqlite3.enable_callback_tracebacks(True)
        lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
        lib.sqlite3_config(4, 1)
        lib.sqlite3_initialize()
        lib.sqlite3_enable_shared_cache(1)
        lib.sqlite3_trace(None, my_cb)
        lib.sqlite3_trace(None, my_cb2)
        lib.sqlite3_trace(None, my_cb3)
        lib.sqlite3_shutdown()

