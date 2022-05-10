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

def test_func(tmp):
    my_cb(tmp)

dll = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
cb = dll.sqlite3_enable_load_extension(b"SQLITE_OK")
dll.sqlite3_load_extension.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p]
dll.sqlite3_load_extension.restype = ctypes.c_int

for i in range(100000):
    connection = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    connection.enable_load_extension(True)
    connection.load_extension('mylib')

    test_func(connection)
