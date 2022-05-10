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
    my_threading_local.a.test(1, 2)

    return 1

def my_cb3(p):
    my_threading_local.a.test(1, 2)

    return 1

def my_cb4(a):
    my_threading_local.a.close()

    return 1

def my_cb5(a):
    b = my_threading_local.a

    return 1

def my_cb6(a):
    my_threading_local.a = None

    return 1

class TestThreading(unittest.TestCase):
    def setUp(self):
        self.thread_error = False
        self.lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

    def test_threaded(self):
        self.lib.sqlite3_enable_shared_cache(1)

        my_threading_local.c = self.lib.sqlite3_open_v2(DB_URI,
                
