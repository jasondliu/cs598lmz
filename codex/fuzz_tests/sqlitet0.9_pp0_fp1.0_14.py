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

my_cb = sqlite3.SQLiteError(1, "a", 1)

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

callbacks = ctypes.cast((ctypes.c_int * 2)(my_cb, 0), ctypes.c_void_p)
rc = lib.sqlite3_config(1, callbacks, 0)

assert rc == 0

conn = sqlite3.connect(DB_URI, uri=True)
assert my_threading_local.a is conn
assert next(conn.iterdump()) == 'CREATE TABLE abc (a PRIMARY KEY)'
assert conn.execute("SELECT test(1, 2)").fetchone()[0] == 1

cursor2 = conn.cursor()
assert cursor2.execute("SELECT test(1, 2)").fetchone()[0] == 1

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
a.create_function("test", 2, lambda a,
