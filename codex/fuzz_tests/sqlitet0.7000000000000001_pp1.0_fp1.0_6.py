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

def test_fn(a, b):
    return a

libc = ctypes.CDLL(ctypes.util.find_library('c'))
libc.pthread_key_create.argtypes = [ctypes.POINTER(ctypes.c_long), ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)]
libc.pthread_key_create.restype = ctypes.c_int

key = ctypes.c_long()
libc.pthread_key_create(ctypes.byref(key), my_cb)

conn = sqlite3.connect(DB_URI, uri=True)
conn.create_function("test", 2, test_fn)

if key.value != 0:
    assert key.value == 1

assert my_threading_local.a is not None

my_threading_local.a.execute("select test(1, 2)")
