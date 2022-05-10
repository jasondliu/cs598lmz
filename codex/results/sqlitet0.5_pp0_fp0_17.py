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

def test_sqlite3_load_extension():
    lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    lib.sqlite3_enable_load_extension(my_threading_local.a.dbapi_connection, 1)
    lib.sqlite3_load_extension(my_threading_local.a.dbapi_connection,
                               "./libsqlitefunctions.so",
                               "sqlite3_extension_init",
                               ctypes.byref(ctypes.c_int(0)))
    cur = my_threading_local.a.cursor()
    cur.execute("select test(?);", (2,))
    assert cur.fetchone()[0] == 2

def test_sqlite3_load_extension_2():
    lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    lib.sqlite3_enable_load_extension(my_threading_local.a.dbapi_connection,
