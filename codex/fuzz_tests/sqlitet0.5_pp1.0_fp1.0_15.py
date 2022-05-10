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
    lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    lib.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_char_p]
    lib.sqlite3_open_v2.restype = ctypes.c_int

    db = ctypes.c_void_p()
    zErrMsg = ctypes.c_char_p()
    ret = lib.sqlite3_open_v2(DB_URI, ctypes.byref(db), 8, None)
    if ret:
        raise sqlite3.OperationalError(f"sqlite3_open_v2() failed: {zErrMsg.value}")

    lib.sqlite3_create_function(db, "my_cb", 1, None, my_cb, None, None)

    lib.sqlite3_close(db
