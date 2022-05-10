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

def my_step_cb(p):
    a = my_threading_local.a

    if a.execute("select test(1, ?);", (2,)).fetchall():
        return 1
    else:
        return 0

def my_final_cb(p):
    a = my_threading_local.a
    a.close()

    return 0

if __name__ == "__main__":
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

    lib.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]
    lib.sqlite3_open.restype = ctypes.c_int

    lib.sqlite3_exec.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char_p)]
    lib.sqlite3
