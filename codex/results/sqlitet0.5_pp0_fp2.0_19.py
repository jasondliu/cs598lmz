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

class Test(unittest.TestCase):
    def setUp(self):
        self.lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
        self.lib.sqlite3_enable_shared_cache(1)
        self.lib.sqlite3_config(3, my_cb, 0)
        self.lib.sqlite3_initialize()

    def tearDown(self):
        self.lib.sqlite3_shutdown()

    def test_function(self):
        conn = sqlite3.connect(DB_URI, uri=True)
        conn.create_function("test", 1, lambda a: a)
        conn.execute("select test(1)")
        conn.close()

    def test_threads(self):
        def f():
            conn = sqlite3.connect(DB_URI, uri=True)
            conn.execute("select test(1, 2)")
            conn.close()

        threads = []
        for i in range(10):
            threads.append(
