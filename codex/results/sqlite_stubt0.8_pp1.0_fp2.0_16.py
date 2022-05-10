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
    cb = my_cb
    cb_p = ctypes.cast(cb, ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p))

    gdbm = ctypes.cdll.LoadLibrary(ctypes.util.find_library('gdbm'))
    gdbm.gdbm_open.restype = ctypes.c_void_p
    gdbm.gdbm_open.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, cb_p, ctypes.c_void_p]
    gdbm.gdbm_close.argtypes = [ctypes.c_void_p]

    gdbm_t = gdbm.gdbm_open(b'test', 0, 0, 1, cb_p, ctypes.c_void_p())

    t = threading.Thread(target=gdbm_t.__del__)
    t
