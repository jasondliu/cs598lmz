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

class Test_spatialite(unittest.TestCase):
    def setUp(self):
        self.handle = sqlite3.sqlite_version_info
        self.handle_type = ctypes.c_int

        self.lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
        self.lib.sqlite3_auto_extension.restype = self.handle_type
        self.lib.sqlite3_auto_extension.argtypes = [ctypes.c_void_p]

    def test_spatialite(self):
        version = sqlite3.sqlite_version_info
        if sqlite3.sqlite_version_info < (3, 5, 9):
            self.fail("cannot perform this test with sqlite %r" % (version,))

        self.lib.sqlite3_auto_extension(my_cb)

        try:
            c = sqlite3.connect(DB_URI)
            a = c.execute("select test(1, 2);").fetchone()
