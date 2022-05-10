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

def main():
    sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(ctypes.c_void_p()), 0x0004 | 0x0001, None)
    sqlite3.sqlite3_close(0)
    sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(ctypes.c_void_p()), 0x0004 | 0x0001, None)

    sqlite3.create_collation("test", 0, my_cb)

    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    conn.execute("CREATE TABLE test (value)")

    conn.execute("INSERT INTO test VALUES ('a')")
    conn.execute("INSERT INTO test VALUES ('b')")
    conn.execute("INSERT INTO test VALUES ('c')")

    conn.execute("SELECT test(value, 'test') FROM test ORDER BY value COLLATE test")

    for row in conn:
        pass


