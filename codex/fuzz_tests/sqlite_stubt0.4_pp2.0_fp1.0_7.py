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

if __name__ == "__main__":
    sqlite3.enable_callback_tracebacks(True)

    test_dll = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    test_dll.sqlite3_config(ctypes.c_int(4), ctypes.c_int(1))

    test_dll.sqlite3_initialize()

    # create a test database
    conn = sqlite3.connect(DB_URI, uri=True)
    conn.close()

    test_dll.sqlite3_create_function_v2(
        ctypes.c_void_p(0),
        ctypes.c_char_p(b"my_cb"),
        ctypes.c_int(1),
        ctypes.c_int(1),
        ctypes.c_void_p(0),
        ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb),
        ctypes.c_void_p(0),
       
