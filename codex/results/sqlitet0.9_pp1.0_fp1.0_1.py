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

def test_connection_leaking_reloaded_extension():
    conn = sqlite3.connect(DB_URI, uri=True)
    sqlite3.SQLITE_EXTENSION_INIT1 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_enable_load_extension(conn, 1)
    lib.sqlite3_load_extension(conn, b"/tmp/sqlite3cef947d0b8abec81a95a8212f46d48da", 0, None)

    assert my_threading_local.a is None

    conn.executescript("SELECT test(1, 2);")

    assert not my_threading_local.a.closed

    del my_threading_local.a

def test_connection_leaking_autoreload_extension():
    conn = sqlite3.connect(DB_
