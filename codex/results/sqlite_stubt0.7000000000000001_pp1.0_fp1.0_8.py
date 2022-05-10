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
    libc = ctypes.CDLL(ctypes.util.find_library("c"))
    #libc.fopen.argtypes = (ctypes.c_char_p, ctypes.c_char_p)
    #libc.fopen.restype = ctypes.c_void_p
    #libc.fclose.argtypes = (ctypes.c_void_p,)

    callback = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)
    sqlite3.sqlite3_initialize()
    sqlite3.sqlite3_config(ctypes.c_int(2), ctypes.c_int(128), callback, ctypes.c_void_p())

    conn = sqlite3.connect(":memory:", factory=deleting_conn)
    c = conn.cursor()
    c.execute("select test(?, ?)", (1, 2))
    assert c.fetchone()[0] == 1

    conn.close()

    sqlite3.sqlite3
