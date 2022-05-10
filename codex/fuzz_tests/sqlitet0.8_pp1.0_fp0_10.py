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


def another_cb(a):
    b = my_threading_local.a
    if b.execute("select test(2, 3);").fetchall()[0][0] != 2:
        return 0
    else:
        return 1


dll = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
fn_ptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.py_object)(my_cb)

my_threading_local.a = None

ret = dll.sqlite3_open(DB_URI.encode("utf-8"), ctypes.byref(pdb))
if ret:
    raise OSError(ret, "Error")

ret = dll.sqlite3_create_function_v2(
        pdb,
        b"another", 1,
        0,
        None,
        ctypes.cast(fn_ptr, ctypes.c_void_p),
        ctypes.cast(fn_ptr, ctypes.c_void_p
