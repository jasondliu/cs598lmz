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

class TestCase(BaseTestCase):
    def setUp(self):
        try:
            from pysqlite2 import dbapi2 as sqlite
        except ImportError:
            self.skipTest("pysqlite not installed")
        self.lib = ctypes.CDLL("libsqlite3-0.dll")
        assert self.lib._name

    def tearDown(self):
        del my_threading_local.a

    def test_race(self):
        self.lib.sqlite3_func_callback(ctypes.CFUNCTYPE(ctypes.c_int)(my_cb))
        conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        cur = conn.cursor()
        cur.execute("select test(1, 1)")
        rs = cur.fetchone()
