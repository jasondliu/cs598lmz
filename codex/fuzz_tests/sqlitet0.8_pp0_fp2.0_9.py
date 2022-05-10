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

sqlite3.sqlite3_enable_shared_cache(True)

try:
    libc = ctypes.CDLL(ctypes.util.find_library('c'))
except Exception:
    pass
else:
    LIBC_THREAD_CREATE_RETURN_VOID = libc.clone
    LIBC_THREAD_CREATE_RETURN_INT  = libc.pthread_create
    LIBC_THREAD_CREATE_RETURN_UINT = libc.clone
    LIBC_THREAD_CREATE_RETURN_PTR  = libc.clone

def create_thread(fn, *args):
    if LIBC_THREAD_CREATE_RETURN_VOID:
        pass
    elif LIBC_THREAD_CREATE_RETURN_INT:
        pass
    else:
        my_threading_local.gce = LIBC_THREAD_CREATE_RETURN_PTR(0, fn, args)

sqlite3.sqlite3_shutdown()

def create_thread_and
