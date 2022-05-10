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

class TestSQLite:
    def setup_class(self):
        self.stderr = None

    def teardown_class(self):
        if self.stderr is not None:
            print(self.stderr.getvalue())

    def test_sqlite3(self):
        dll = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

        self.stderr = io.StringIO()
        sys.stderr = self.stderr

        ret = ctypes.c_int()
        self.assertEqual(0, dll.sqlite3_enable_shared_cache(1, ctypes.byref(ret)))
        self.assertNotEqual(0, ret.value)

        ret = ctypes.c_int()
        self.assertEqual(0, dll.sqlite3_initialize())
        ret = ctypes.c_int()
        self.assertEqual(0, dll.sqlite3_config(0, 1, ctypes.byref(ret)))

