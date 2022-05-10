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

class MyTestCase(unittest.TestCase):
    def test_1(self):
        sqlite3.enable_callback_tracebacks(True)
        sqlite3.enable_shared_cache(True)
        self.assertEqual(1, sqlite3.threadsafety())
        self.assertEqual(1, sqlite3.thread_cleanup())

        sqlite3.thread_cleanup()

        sqlite3.thread_cleanup()

        ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_thread_cleanup()

        a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

        def test_fn(a, b):
            return a

        a.create_function("test", 2, test_fn)

        my_threading_local.a = a

        sqlite3.thread_cleanup()

        sqlite3.thread_cleanup()

        sqlite3.thread_cleanup()

        ctypes.CDLL(ctypes.
