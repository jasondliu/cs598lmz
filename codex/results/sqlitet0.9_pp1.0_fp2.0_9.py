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
    def test_check_callback(self):
        sqlite3.enable_callback_tracebacks(True)
        sqlite3.SQLITE_MAX_WORKER_THREADS = 0
        sqlite3.enable_shared_cache(False)

        x = ctypes.c_int.in_dll(ctypes.CDLL(ctypes.util.find_library("sqlite3")), "main_thread")
        old_value = x.value

        self.assertEqual(old_value, 0)

        conn = sqlite3.connect(DB_URI, uri=True)

        self.assertEqual(x.value, 0)

        conn.set_progress_handler(my_cb, 2)
        #conn.create_function("test", 2, my_cb)

        self.assertEqual(x.value, 0)

        #conn.execute("select test(1, 2)").fetchone()

        del conn

        self.assertEqual(x.value, 0)



