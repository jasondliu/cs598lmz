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


def test_threading():
    lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    lib.sqlite3_open(':memory:', ctypes.byref(ctypes.c_void_p()))
    lib.sqlite3_enable_load_extension(my_threading_local.a.cursor().connection.connection, 1)
    lib.sqlite3_load_extension(my_threading_local.a.cursor().connection.connection,
                               "./test_extension/extension.so", "sqlite3_extension_init", ctypes.byref(ctypes.c_char_p()))
    # enable_load_extension is turned off again here, because it's not thread-safe
    lib.sqlite3_enable_load_extension(my_threading_local.a.cursor().connection.connection, 0)
    c = my_threading_local.a.cursor()
    c.execute("select test(23, 42)")
    res = c
