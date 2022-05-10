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

def my_cb_dealloc(p):
    my_threading_local.a.__del__()
    return 1

def main():
    sqlite3.sqlite3_open_v2
    sqlite3.sqlite3_thread_cleanup
    sqlite3.sqlite3_initialize
    sqlite3.sqlite3_shutdown
    sqlite3.sqlite3_config
    sqlite3.sqlite3_win32_set_directory

    lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    lib.sqlite3_config(0x01)

    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.create_function("test_cb", 1, my_cb)
    a.create_function("test_cb_dealloc", 1, my_cb_dealloc)

    a.execute("select test_cb(1)")
    my_threading_local.a.execute("select test(1, 2
