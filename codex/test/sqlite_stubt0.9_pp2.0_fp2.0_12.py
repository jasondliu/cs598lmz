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

def free_cb(p):
    print("Freeing", p)

    return 1

def test_crash():
    lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    lib.sqlite3_enable_shared_cache(1)

    assert lib.sqlite3_uri_boolean(DB_URI, "shared_cache", 0)

    x = ctypes.c_int()

    conn = ctypes.c_void_p()
    assert lib.sqlite3_open_v2(":memory:", ctypes.byref(conn), 0 | 0x4000000, None) == 0

    assert lib.sqlite3_open_aux_file(conn, None, None) is not None
    assert lib.sqlite3_autocommit_v2(conn, 1)

    assert lib.sqlite3_config(2, my_cb, ctypes.byref(x), free_cb) == 0

