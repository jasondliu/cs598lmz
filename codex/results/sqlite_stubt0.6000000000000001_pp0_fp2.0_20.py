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
    def setUp(self):
        self.sqlite = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
        self.sqlite.sqlite3_config(ctypes.c_int(4), ctypes.c_int(1))
        self.sqlite.sqlite3_open_v2(
            b":memory:",
            ctypes.byref(self.sqlite.sqlite3_open_v2.argtypes[1]),
            ctypes.c_int(0x01 | 0x04),
            ctypes.c_void_p()
        )

        self.sqlite.sqlite3_create_function(
            self.sqlite.sqlite3_open_v2.argtypes[1].value,
            b"test",
            2,
            ctypes.c_int(0x02),
            ctypes.c_void_p(-1),
            my_cb,
            None,
            None,
            ctypes.c_
