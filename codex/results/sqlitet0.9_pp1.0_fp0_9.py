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

def my_cb_next(p):
    return 1

class TestGFunction:
    def setUp(self):
        self.lib = ctypes.CDLL(ctypes.util.find_library("mark9"))

        self.lib.mark9_init.restype = ctypes.c_int
        self.lib.mark9_init.argtypes = [ctypes.c_int]
        assert self.lib.mark9_init(0)
        self.lib.mark9_set_db_uri(DB_URI)

        self.lib.mark9_add_callback.restype = ctypes.c_int
        self.lib.mark9_add_callback.argtypes = [ctypes.c_int]
        self.lib.mark9_register_callback.restype = ctypes.c_int
        self.lib.mark9_register_callback.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_char_p]
        self.lib.mark9_bb_start_next.restype =
