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

try:
    sqlite3.enable_shared_cache(True)
    sqlite3.sqlite3_disable_shared_cache(False)

    try:
        libc = ctypes.CDLL(ctypes.util.find_library('c'))
    except:
        libc = ctypes.CDLL('libc.so.6')
    libc.pthread_create.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

    cb = sqlite3.SQLiteCallback(my_cb)
    p = ctypes.create_string_buffer(4)
    libc.pthread_create(p, None, cb, None)
    libc.pthread_join(p, None)
except:
    # disable shared cache if we can't test it
    sqlite3.enable_shared_cache(False)
    sqlite3.sqlite3_disable_shared_cache(True)
