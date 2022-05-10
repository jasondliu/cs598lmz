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


def my_cb2(n, p, p2):
    del my_threading_local.a

    return 0

sqlite3.sqlite3_open_v2(":memory:", ctypes.byref(my_threading_local.e), 0x00000002 | 0x00000001, ctypes.c_char_p(DB_URI.encode('utf-8')))
sqlite3.sqlite3_update_hook(my_threading_local.e.value, my_cb2, None)
sqlite3.sqlite3_commit_hook(my_threading_local.e.value, my_cb, None)

if sqlite3.sqlite3_exec(my_threading_local.e.value, "CREATE TABLE x(y);", 0, 0, 0) != 0:
    raise Exception("Could not create table")

if sqlite3.sqlite3_exec(my_threading_local.e.value, "INSERT INTO x VALUES(test(1,2));", 0, 0, 0) != 0
