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

def my_auth(a, b, c, d, e, f):
    return 0

def my_close(a):
    sqlite3.register_authorizer(None)
    sqlite3.register_progress_handler(None)
    my_threading_local.a = None

libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.__libc_fork()

libc.__register_atfork(None, None, my_close, None)

sqlite3.register_authorizer(my_auth)
sqlite3.register_progress_handler(my_cb)
