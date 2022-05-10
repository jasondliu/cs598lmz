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

def my_cb2(p):
    my_threading_local.a.execute("SELECT test(?, ?)", (1, 2))
    return 0

def main():
    sqlite3.enable_callback_tracebacks(True)
    assert sqlite3.threadsafety == 0

    c_lib = ctypes.CDLL(ctypes.util.find_library("c"))
    c_lib.call_cb_loop.argtypes = (ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p),)
    c_lib.call_cb_loop.restype = None

    c_lib.call_cb_loop(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb2))
    c_lib.call_cb_loop(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb))

if __name__ == "__main__":
    main()
