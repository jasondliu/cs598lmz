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

my_cb_p = sqlite3.SQLITE_DETERMINISTIC | sqlite3.SQLITE_UTF8 | sqlite3.SQLITE_INNOCUOUS | sqlite3.SQLITE_SUBTYPE

sqlite3.sqlite3_set_authorizer(my_cb, my_cb_p)

sqlite3.sqlite3_test_control(sqlite3.SQLITE_TESTCTRL_OPTIMIZATIONS, 0, 1)
sqlite3.sqlite3_test_control(sqlite3.SQLITE_TESTCTRL_OPTIMIZATIONS, 0, 2)
sqlite3.sqlite3_test_control(sqlite3.SQLITE_TESTCTRL_OPTIMIZATIONS, 0, 3)
sqlite3.sqlite3_test_control(sqlite3.SQLITE_TESTCTRL_OPTIMIZATIONS, 0, 4)
