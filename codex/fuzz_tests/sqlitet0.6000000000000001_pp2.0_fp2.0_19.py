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

class TestCtypes(unittest.TestCase):
    def test_init_finalize(self):
        self.assertTrue(hasattr(sqlite3._sqlite3, "sqlite3_initialize"))
        sqlite3._sqlite3.sqlite3_initialize()
        self.assertTrue(hasattr(sqlite3._sqlite3, "sqlite3_shutdown"))
        sqlite3._sqlite3.sqlite3_shutdown()

    def test_open(self):
        sqlite3._sqlite3.sqlite3_open(":memory:", ctypes.byref(ctypes.c_void_p()))

    def test_enable_load_extension(self):
        self.assertTrue(hasattr(sqlite3._sqlite3, "sqlite3_enable_load_extension"))
        con = sqlite3.connect(":memory:")
        try:
            con.enable_load_extension(True)
            con.load_extension(ctypes.util.find_library("sqlite3"))

