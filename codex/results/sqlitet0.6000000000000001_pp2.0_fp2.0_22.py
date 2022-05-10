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

p = ctypes.c_void_p()

sqlite3.sqlite3_open_v2(":memory:", ctypes.byref(p), 0x0001 | 0x0008, None)

sqlite3.sqlite3_prepare_v2(p, "SELECT test(1, 2)", len("SELECT test(1, 2)"), ctypes.byref(p), None)

sqlite3.sqlite3_exec(p, "PRAGMA soft_heap_limit=0", None, None, None)

sqlite3.sqlite3_create_function_v2(p, b"test", 2, 1, None, my_cb, None, None, None)

sqlite3.sqlite3_step(p)

sqlite3.sqlite3_exec(p, "PRAGMA soft_heap_limit=0", None, None, None)

sqlite3.sqlite3_step(p)

sqlite3.sqlite3_finalize(p)

sqlite3.sqlite3_
