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

def main():
    sqlite_path = ctypes.util.find_library("sqlite3") or "sqlite3"
    sqlite = ctypes.CDLL(sqlite_path)

    sqlite.sqlite3_enable_uri(1)
    sqlite.sqlite3_db_config(ctypes.c_void_p(), 10, 1, ctypes.c_void_p())

    sqlite.sqlite3_open_v2(":memory:",
                           ctypes.byref(ctypes.c_void_p()),
                           3,
                           None)

    sqlite.sqlite3_uri_boolean(ctypes.c_char_p(DB_URI),
                               ctypes.c_char_p("autocommit"),
                               0)

    sqlite.sqlite3_mutex_alloc(ctypes.c_int())
    sqlite.sqlite3_initialize()
