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
        self.lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
        self.lib.sqlite3_config(SQLITE_CONFIG_URI, 1)
        self.lib.sqlite3_config(SQLITE_CONFIG_LOG, my_cb)

    def test_log_callback(self):
        conn = sqlite3.connect(DB_URI, uri=True)
        conn.execute("select test(1, 2)")
        conn.close()

        self.assertTrue(hasattr(my_threading_local, 'a'))
        self.assertTrue(my_threading_local.a is not None)
        self.assertTrue(my_threading_local.a.execute("select 1").fetchone()[0] == 1)
        self.lib.sqlite3_close(my_threading_local.a.connection)
        self.assertTrue(my_threading_local.a.connection is None)
