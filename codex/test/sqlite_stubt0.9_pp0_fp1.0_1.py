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

libpthread = ctypes.CDLL(ctypes.util.find_library("pthread"), use_errno=True)

libpthread.pthread_setspecific.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
libpthread.pthread_setspecific.restype = ctypes.c_int

pthread_key = ctypes.c_uint32()

libpthread.pthread_key_create(ctypes.byref(pthread_key), None)

libpthread.pthread_setspecific(pthread_key, ctypes.pythonapi.PyCapsule_New(my_cb, None, None))

with sqlite3.connect(DB_URI, uri=True) as conn:
    cur = conn.cursor()
    cur.execute("SELECT test(1, 2)")
    cur.execute("SELECT test(1, 2)")

print(my_threading_local.a)

del my_threading_local

del cur
