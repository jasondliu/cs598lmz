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

class sqlite3_threading_local(unittest.TestCase):
    def test_threading_local(self):
        lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
        self.assertTrue(hasattr(lib, 'sqlite3_thread_cleanup'))
        lib.sqlite3_thread_cleanup()
        lib.sqlite3_thread_cleanup() # make sure it doesn't crash
        self.assertTrue(hasattr(lib, 'sqlite3_config'))
        lib.sqlite3_config(4, my_cb) # SQLITE_CONFIG_SINGLETHREAD
        self.assertTrue(hasattr(lib, 'sqlite3_thread_cleanup'))
        lib.sqlite3_thread_cleanup()
        lib.sqlite3_thread_cleanup() # make sure it doesn't crash

        def fn(i):
            a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
            def test_fn(
