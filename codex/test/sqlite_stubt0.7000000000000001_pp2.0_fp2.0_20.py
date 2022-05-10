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

def my_cb_val(n):
    return 1

class my_cb_callable(object):
    def __call__(self, p):
        return 1

def my_cb_val_callable():
    return 1

@unittest.skipUnless(sqlite3.sqlite_version_info >= (3,8,3),
                     "requires sqlite 3.8.3 or later")
class MyTest(unittest.TestCase):
    def test_plain(self):
        self.assertEqual(1, sqlite3.enable_callback_tracebacks(1))
        self.assertEqual(0, sqlite3.enable_callback_tracebacks(0))

    def test_startswith(self):
        self.assertTrue(sqlite3.sqlite_version.startswith("3."))
        self.assertTrue(sqlite3.sqlite_version_info.startswith((3,)))

