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

def run_tests():
    SQLITE_STATIC = ctypes.c_int.in_dll(ctypes.CDLL(ctypes.util.find_library("sqlite3")), "SQLITE_STATIC").value
    sqlite3.sqlite3_set_authorizer(my_cb, SQLITE_STATIC)

    # calls my_cb
    my_threading_local.a.execute("ALTER TABLE test ADD COLUMN test1 test")

    # doesn't call my_cb
    my_threading_local.a.execute("ALTER TABLE test ADD COLUMN test2 test")

for i in range(3):
    print "test", i
    run_tests()
</code>

