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
    a = my_threading_local.a

    assert a.execute("select test(1, 2)").fetchone()[0] == 1

    return 1

def main():
    libc = ctypes.CDLL(ctypes.util.find_library("c"))
    libc.pthread_key_create.argtypes = [
        ctypes.POINTER(ctypes.c_long), ctypes.c_void_p]
    libc.pthread_setspecific.argtypes = [ctypes.c_long, ctypes.c_void_p]
    libc.pthread_getspecific.argtypes = [ctypes.c_long]
    libc.pthread_getspecific.restype = ctypes.c_void_p

    key = ctypes.c_long()
    libc.pthread_key_create(ctypes.byref(key), None)

    libc.pthread_setspecific(key.value, ctypes.py_object(my_cb))
