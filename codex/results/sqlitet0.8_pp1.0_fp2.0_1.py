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

lib = ctypes.CDLL('libtest-db-closure.so')
lib.connection_ptr.argtypes = []
lib.connection_ptr.restype = ctypes.c_void_p

lib.create_connection.argtypes = [ctypes.c_void_p]
lib.create_connection.restype = ctypes.c_void_p

lib.connection_close.argtypes = [ctypes.c_void_p]
lib.connection_close.restype = None

lib.connection_begin.argtypes = [ctypes.c_void_p]
lib.connection_begin.restype = None

lib.connection_prepare.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
lib.connection_prepare.restype = ctypes.c_void_p

lib.connection_exec.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
lib.connection_exec.restype = None

lib.statement_bind.argtypes = [ct
