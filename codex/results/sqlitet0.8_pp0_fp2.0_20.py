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

my_cb_ptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

class SQLiteThread:
    def __init__(self, uri, cb=None, step=100):
        if cb == None:
            cb = my_cb_ptr
        self.uri = uri
        self.cb = cb
        self.step = step
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def run(self):
        libsqlite_path = ctypes.util.find_library('sqlite3')
        libsqlite = ctypes.CDLL(libsqlite_path)

        def arg(x):
            if isinstance(x, int):
                return ctypes.c_int(x)
            elif isinstance(x, float):
                return ctypes.c_double(x)
            elif isinstance(x, str):
                return ctypes.c_char_p(x)

