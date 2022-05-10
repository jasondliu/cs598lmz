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


class MyTest(unittest.TestCase):
    def test_one(self):
        a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

        a.execute("CREATE TABLE foo(x)")
        a.execute("INSERT INTO foo(x) VALUES (?)", ("testing",))

        my_threading_local.a = a

        self.assertEqual(a.execute("SELECT test(x) FROM foo").fetchall(), [("testing",)])

        p = ctypes.PythonAPI(sqlite3)
        p.sqlite3_create_module.restype = ctypes.c_int
        p.sqlite3_create_module.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(sqlite3.sqlite3_module)]

        p.sqlite3_open_v2.restype = ctypes.c_int
        p.sqlite3_open_v2.argtypes = [
            ctypes
