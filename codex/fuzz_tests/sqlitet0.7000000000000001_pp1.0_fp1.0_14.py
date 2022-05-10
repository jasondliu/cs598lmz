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

def my_cb_del(p):
    my_threading_local.a.close()
    return 1

class TestFunc(unittest.TestCase):
    def setUp(self):
        sqlite3.enable_callback_tracebacks(True)
        self.sqlite_db = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def tearDown(self):
        self.sqlite_db.close()

    def _test_callback(self, cb, *args):
        cb_ptr = sqlite3.sqlite3_callback_ptr(cb)
        self.assertTrue(bool(cb_ptr))
        fn = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, *args)(cb_ptr)
        res = fn(None)
        self.assertEquals(res, 1)

    def _test_callback_del(self, cb, *args):
        cb_ptr = sqlite3.sqlite3_
