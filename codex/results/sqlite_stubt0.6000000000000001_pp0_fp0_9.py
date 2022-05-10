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
    my_threading_local.a.close()
    return 1

if __name__ == '__main__':
    sqlite3.enable_callback_tracebacks(True)

    libc = ctypes.CDLL(ctypes.util.find_library('c'))
    libc.pthread_create.restype = ctypes.c_int

    sqlite3.threadsafety = 2
    sqlite3.threading = False
    sqlite3.sqlite_version_info = (3, 7, 0)

    db = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    db.create_function("my_cb", 0, my_cb)
    db.create_function("my_cb2", 0, my_cb2)

    libc.pthread_create(None, None, my_cb, None)

    db.execute("select my_cb()")

    libc.pthread_create(None, None, my_cb2, None)


