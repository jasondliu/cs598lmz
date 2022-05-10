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

if __name__ == '__main__':
    # https://groups.google.com/d/msg/sqlite-users/e0H_iCm0izE/zElC2QPwAQAJ
    # https://gist.github.com/malcom/be082d07aa8cef47dc6a
    lib = ctypes.util.find_library("sqlite3")
    sqlite3 = ctypes.CDLL(lib)

    p = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)

    sqlite3.sqlite3_initialize()

    sqlite3.sqlite3_config(0x0)
    sqlite3.sqlite3_config(0x001, p)
    sqlite3.sqlite3_config(0x002, p)
    sqlite3.sqlite3_config(0x003, p)

    db = sqlite3.sqlite3_open_v2(b'file:test.db?mode=memory', ctypes.byref(
