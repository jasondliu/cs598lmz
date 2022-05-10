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

def my_cb_final(p):
    my_threading_local.a.close()
    return 1

class MyTest(unittest.TestCase):
    def test_threads(self):
        lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
        lib.sqlite3_initialize()
        lib.sqlite3_shutdown()

        lib.sqlite3_config(ctypes.c_int(lib.SQLITE_CONFIG_URI), 1)
        lib.sqlite3_config(ctypes.c_int(lib.SQLITE_CONFIG_MULTITHREAD))

        lib.sqlite3_enable_shared_cache(1)

        lib.sqlite3_auto_extension(my_cb)
        lib.sqlite3_auto_extension(my_cb_final)

        threads = []
        for i in range(5):
            t = threading.Thread(target=lambda: sqlite3.connect(DB_URI, uri=True))
