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

sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(my_threading_local.p), 1 | 2, None)
sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(my_threading_local.p2), 1 | 2, None)
sqlite3.sqlite3_progress_handler(my_threading_local.p, 5, my_cb, None)
sqlite3.sqlite3_progress_handler(my_threading_local.p2, 5, my_cb, None)

def my_fn(p):
    my_threading_local.a.cursor().execute("select test('asdf', 'asdf2')")
    return 0

sqlite3.sqlite3_busy_handler(my_threading_local.p, my_fn, None)
sqlite3.sqlite3_busy_handler(my_threading_local.p2, my_fn, None)


def run():
    for i in xrange(
