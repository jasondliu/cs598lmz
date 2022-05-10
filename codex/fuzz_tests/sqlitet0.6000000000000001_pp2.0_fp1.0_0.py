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

sqlite3.sqlite3_shutdown()
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, True)
sqlite3.sqlite3_initialize()
sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(my_threading_local.p),
    sqlite3.SQLITE_OPEN_READWRITE | sqlite3.SQLITE_OPEN_CREATE | sqlite3.SQLITE_OPEN_URI, None)

my_threading_local.p = my_threading_local.p.value

sqlite3.sqlite3_busy_handler(my_threading_local.p, my_cb, None)

def main():
    with sqlite3.connect(DB_URI, uri=True) as conn:
        conn.execute("create table t (a int)")
        conn.execute("insert into t (a) values (1)")
        conn.execute("insert into t (a) values (2)")
        conn.
