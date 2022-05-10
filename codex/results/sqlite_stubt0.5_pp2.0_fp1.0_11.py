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

p = sqlite3.SQLiteConnection(DB_URI, uri=True, factory=deleting_conn)

libc = ctypes.CDLL(ctypes.util.find_library("c"))

libc.pthread_create.argtypes = [
    ctypes.POINTER(ctypes.c_void_p),
    ctypes.c_void_p,
    ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p),
    ctypes.c_void_p,
]

t = ctypes.c_void_p()

libc.pthread_create(ctypes.byref(t), None, my_cb, None)

libc.pthread_join(t, None)

my_threading_local.a.close()
del my_threading_local.a

p.close()
</code>
The output is:
<code>$ python3 test.py
test.py:30: RuntimeWarning: SQLite objects created in threads can only be used in
