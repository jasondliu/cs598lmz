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


class TestLine(unittest.TestCase):
    def setUp(self,):
        if "sqlite" in globals():
            del globals()["sqlite"]

        self.c_buffer = ctypes.create_string_buffer(0)

        my_cb_c = ctypes.CFUNCTYPE(None, ctypes.c_void_p)(my_cb)
        api_fn = ctypes.c_void_p.in_dll(lib, "sqlite3_updatehook")
        c_api_callable = ctypes.cast(api_fn, ctypes.CFUNCTYPE(None, ctypes.c_void_p))
        self.fn = my_cb_c

        self.result = c_api_callable(self.fn)

        import sqlite3
        import flask_sqlite3

        self.con = sqlite3.connect(DB_URI, uri=True)

    def tearDown(self):
        self.fn = None
        self.c_buffer = None
        del self.result

