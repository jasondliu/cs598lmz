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

# Callback to try to close any sqlite3 connection, to avoid
# ResourceWarning exceptions.
def stop_cb(p):
    # Return code doesn't matter here.
    try:
        my_threading_local.a.close()
        del my_threading_local.a
    except Exception:
        pass
    return 1

def main():
    # Import, but avoid "used" warning.
    pytest = __import__("pytest")

    # Link the callback and our `test_fn()`.
    ll = ctypes.cdll.LoadLibrary(ctypes.util.find_library("guv"))
    ll.guv_expose_py_cb()
    funcptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_voidp)(my_cb)
    ll.guv_py_cb_1(funcptr, ctypes.c_voidp(0))
    funcptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_voidp)(stop_cb)
