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


def my_cb_simple(p):
    my_threading_local.a = "hello"
    return 1


def my_cb_async(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    return 1


def my_cb_async_simple(p):
    my_threading_local.a = "hello"
    return 1


def get_libsqlite3():
    try:
        libsqlite3 = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    except OSError as e:
        if e.errno == errno.ENOENT:
            raise unittest.SkipTest("sqlite3 not found")
        else:
            raise
    else:
        return libsqlite3


