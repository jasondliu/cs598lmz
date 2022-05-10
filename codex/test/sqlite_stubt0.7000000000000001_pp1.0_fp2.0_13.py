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
    ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)

    my_cb = sqlite3.SQLITE_STATIC(ctypes.PyCFuncPtr(my_cb))

    sqlite3.sqlite3_initialize()
    sqlite3.sqlite3_open_v2(":memory:", ctypes.pointer(my_threading_local.a), sqlite3.SQLITE_OPEN_READWRITE | sqlite3.SQLITE_OPEN_CREATE, None)

    my_threading_local.a.executescript("""
        CREATE TABLE test(i INTEGER);
        INSERT INTO test VALUES(test(5, 0));
    """)

    print(list(my_threading_local.a.execute("SELECT i FROM test;")))
    my_threading_local.a.close()

