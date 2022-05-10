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

_l = sqlite3.sqlite_version_info
sqlite3.sqlite_version_info = _l + (None,)

sqlite3.sqlite3_threadsafe()

sqlite3.sqlite3_enable_shared_cache(True)
ld = ctypes.cdll[ctypes.util.find_library('sqlite3')]
ld.sqlite3_shutdown()
ld.sqlite3_initialize()

sqlite3.sqlite3_config(29, 1)

sqlite3.sqlite3_config(45, my_cb, None)

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

def test_fn(a, b):
    return a

a.create_function("test", 2, test_fn)

my_threading_local.a = a

def call_fn(x, y):
    ret = x.execute("select test(?,?)", (y, 1)).fetchall()[0][0]
    assert
