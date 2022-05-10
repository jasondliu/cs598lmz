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

libpthread = ctypes.CDLL(ctypes.util.find_library('pthread'))
libpthread.pthread_create.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
libpthread.pthread_create.restype = ctypes.c_int

libsqlite3 = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

libsqlite3.sqlite3_enable_shared_cache(1)

libsqlite3.sqlite3_open(DB_URI.encode('utf-8'), ctypes.byref(my_threading_local.db))

libpthread.pthread_create(None, None, my_cb, None)

libsqlite3.sqlite3_close(my_threading_local.db)

del my_threading_local
