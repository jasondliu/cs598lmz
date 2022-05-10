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
    """
    Setup
    """

    def setUp(self):
        self.lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

        self.cb_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)

        self.register_me = self.cb_type(my_cb)

        self.flags = sqlite3.SQLITE_OPEN_URI | sqlite3.SQLITE_OPEN_MEMORY

    """
    Tests!
    """

    def test_threading_local(self):
        self.lib.sqlite3_open_v2("test", sqlite3.sqlite_pp, self.flags, ctypes.c_void_p(0))

        with self.assertRaises(AttributeError) as cm:
            my_threading_local.a

        assert 'has no attribute' in str(cm.exception)

        self.lib.sqlite3_open_v
