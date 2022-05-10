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

def my_cb2(p):
    my_threading_local.a.close()
    return 1

class Test(unittest.TestCase):
    def _load_ext(self):
        my_cb_fn = sqlite3.SQLiteCallback(my_cb)
        my_cb_fn2 = sqlite3.SQLiteCallback(my_cb2)
        r = sqlite3.sqlite3_enable_load_extension(self.con, 1)
        self.assertEquals(r, sqlite3.SQLITE_OK)
        r = sqlite3.sqlite3_load_extension(self.con, "./test.sqlite3", None, my_cb_fn)
        self.assertEquals(r, sqlite3.SQLITE_OK)
        r = sqlite3.sqlite3_load_extension(self.con, "./test.sqlite3", None, my_cb_fn2)
        self.assertEquals(r, sqlite3.SQLITE_OK)

    def _init_db
