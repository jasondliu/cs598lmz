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


def my_cb_destructor(p):
    print("my_cb_destructor", my_threading_local.a)
    my_threading_local.a.close()
    return 0


class SQLiteThreadingTests(unittest.TestCase):
    def setUp(self):
        self.dll = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

    def tearDown(self):
        del self.dll

    def CheckThreading(self):
        self.dll.sqlite3_enable_shared_cache(1)
        self.dll.sqlite3_initialize()
        self.dll.sqlite3_shutdown()
        self.dll.sqlite3_enable_shared_cache(0)

    def test_threading(self):
        self.dll.sqlite3_enable_shared_cache(1)
        self.dll.sqlite3_create_disposable_module.argtypes = (
            ctypes.c_void_p, ctypes.c_char_p, c
