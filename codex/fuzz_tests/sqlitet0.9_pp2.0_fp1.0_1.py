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

def another_test_fn(a, b):
    return b

sqlite3.register_adapter(type(my_threading_local.a), lambda obj: aaaa)


if __name__ == "__main__":
    my_db = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    my_db.create_function("another_test", 2, another_test_fn)

    p = ctypes.c_void_p()
    sqlite3.sqlite3_open_v2(":memory:", ctypes.byref(p), sqlite3.SQLITE_OPEN_READWRITE | sqlite3.SQLITE_OPEN_CREATE | sqlite3.SQLITE_OPEN_URI, None)
    sqlite3.sqlite3_prepare_v2(p, "SELECT another_test(1, test(2, 3))", -1, ctypes.byref(p), ctypes.c_char_p())
    sqlite3.sqlite3_step(p
