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

def my_cb_2(p):
    a = my_threading_local.a

    for i in range(10):
        a.execute("select test(1, 2)")
        a.commit()

    return 1

def test_callback():
    cb = sqlite3.SQLITE_CALLBACK(my_cb)
    cb2 = sqlite3.SQLITE_CALLBACK(my_cb_2)
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_open(":memory:", ctypes.byref(ctypes.c_void_p()))
    lib.sqlite3_exec(my_threading_local.a._sqlite3, "create table test (id int)", cb, 0, 0)
    lib.sqlite3_exec(my_threading_local.a._sqlite3, "insert into test values (1)", cb2, 0, 0)

if __name__ == "__main__":
    test_callback()

