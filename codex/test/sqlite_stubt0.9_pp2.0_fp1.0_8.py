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
    a = my_threading_local.a

    ret = a.cursor().execute("select test(2, 3)").fetchone()[0]
    a.close()
    my_threading_local.a = None

    return ret

p = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3')).sqlite3_enable_load_extension(None, my_cb)
assert p.errno == 0
p = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3')).sqlite3_enable_load_extension(None, my_cb2)
assert p.errno == 0

import _sqlite3
