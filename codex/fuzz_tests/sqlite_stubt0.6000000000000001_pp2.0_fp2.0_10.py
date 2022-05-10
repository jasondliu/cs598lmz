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

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_config(ctypes.c_int(1), ctypes.c_int(1))

lib.sqlite3_open_v2(ctypes.c_char_p(DB_URI), ctypes.c_void_p(), ctypes.c_int(1), ctypes.c_char_p(None))
lib.sqlite3_create_function_v2(ctypes.c_void_p(), ctypes.c_char_p(b"create_fn"), ctypes.c_int(1), ctypes.c_int(0), ctypes.c_void_p(), ctypes.c_void_p(my_cb), ctypes.c_void_p(), ctypes.c_void_p())
lib.sqlite3_close(ctypes.c_void_p())

if __name__ == "__main__":
    print("OK")
