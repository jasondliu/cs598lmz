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

    a.execute("select test(?, ?)", (1, 2))
    return 1

class TestCase(unittest.TestCase):
    def setUp(self):
        self.lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
        self.lib.sqlite3_enable_shared_cache(1)
        self.lib.sqlite3_config(1)

        self.lib.sqlite3_open_v2(DB_URI.encode("utf-8"), ctypes.byref(self.db), 1, None)

    def tearDown(self):
        self.lib.sqlite3_close(self.db)

    def test_threaded_callbacks(self):
        self.lib.sqlite3_enable_load_extension(self.db, 1)
        self.lib.sqlite3_load_extension(self.db, "./extension/src/.libs/extension.so",
