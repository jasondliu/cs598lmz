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
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    return 1

class TestThreading(unittest.TestCase):
    def setUp(self):
        self.lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"), use_errno=True)
        self.lib.sqlite3_initialize()
        self.lib.sqlite3_config(3, 1)

    def tearDown(self):
        self.lib.sqlite3_shutdown()

    def test_threading(self):
        self.lib.sqlite3_config(7, my_cb, None)

        self.lib.sqlite3_threadsafe()

        a = sqlite3.connect(DB_URI, uri=True, factory=deleting
