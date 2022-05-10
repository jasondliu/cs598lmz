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
        self.libc = ctypes.CDLL(ctypes.util.find_library('c'))

    def test_create_function(self):
        self.libc.sqlite3_enable_shared_cache(True)
        self.libc.sqlite3_config(1, my_cb, 0, 0)
        self.libc.sqlite3_initialize()
        try:
            conn = sqlite3.connect(DB_URI, uri=True)
            conn.execute("create table test(id)")
            conn.execute("insert into test values (test(1, 2))")
            conn.commit()
            result = conn.execute("select * from test")
            self.assertEqual(result.fetchone()[0], 1)
        finally:
            self.libc.sqlite3_shutdown()

    def test_create_function_compat(self):
        self.libc.sqlite3_enable_shared_cache(True)
