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

class MyTest(unittest.TestCase):
    def test_thread_local_refcounts(self):
        # Connect to the database to create the schema
        a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        a.close()

        # Create a threading local callback
        sqlite3.enable_callback_tracebacks(True)
        a = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
        a.sqlite3_thread_cleanup()
        self.assertEqual(a.sqlite3_config(ctypes.c_int(4), ctypes.c_void_p(my_cb)), 0)
        self.assertEqual(a.sqlite3_thread_cleanup(), 0)
        a.sqlite3_thread_cleanup()

        # Create a thread and make sure that it is cleaned up
        t = threading.Thread(target=lambda: a.sqlite3_thread_cleanup())
        t.start()
        t.join
