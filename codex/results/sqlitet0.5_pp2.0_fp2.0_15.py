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

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)

libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.pthread_create.argtypes = [ctypes.POINTER(ctypes.c_void_p),
                                ctypes.c_void_p,
                                ctypes.c_void_p,
                                ctypes.c_void_p]

pthread = libc.pthread_create

thread_id = ctypes.c_void_p(0)
pthread(ctypes.byref(thread_id), None, my_cb, None)

libc.pthread_join(thread_id, None)

a = my_threading_local.a

a.close()

print("done")
