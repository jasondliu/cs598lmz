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
    ctypes.pythonapi.PyEval_InitThreads()
    ctypes.pythonapi.PyEval_ReleaseThread(ctypes.pythonapi.PyEval_SaveThread())

    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_config(3)

    lib.sqlite3_open(DB_URI.encode("utf-8"), ctypes.byref(ctypes.c_void_p()))

    lib.sqlite3_create_function_v2(
        ctypes.c_void_p(),
        b"my_cb",
        -1,
        2,
        None,
        ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb),
        None,
        None,
        None
    )

    lib.sqlite3_close(ctypes.c_void_p())

    for i in range(10):
        threading.Thread(target=lambda: my_thread
