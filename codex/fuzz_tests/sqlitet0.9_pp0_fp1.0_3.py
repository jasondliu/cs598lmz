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

p = my_cb
p.__doc__ = b"client_cb"

sqlite3.sqlite3_initialize()
sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_URI), 1)
r = sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_MULTITHREAD), 1)
assert r == 0
r = sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_CLIENT_RESULT_CALLBACK), p)
assert r == 0

def init_db():
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, x);")
    for i in range(1, 10):
        a.execute("INSERT INTO test (id) VALUES (?);", (i,))
    a.execute("SELECT test(1
