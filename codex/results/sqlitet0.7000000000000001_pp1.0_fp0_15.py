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
    p = ctypes.pointer(ctypes.c_int(0))
    lib = ctypes.util.find_library("sqlite3")
    sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_URI), my_cb, p)
    sqlite3.sqlite3_open_v2(b":memory:", ctypes.pointer(sqlite3.sqlite3(None)), ctypes.c_int(0x00000002), None)

    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    cur = a.execute("select test(1, 2)")
    assert cur.fetchone()[0] == 1

    a = my_threading_local.a
    cur = a.execute("select test(1, 2)")
    assert cur.fetchone()[0] == 1

    cur = my_threading_local.a.execute("select test(1, 2)")
    assert cur.fetch
