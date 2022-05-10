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

class MyError(Exception):
    pass

def my_step(p):
    global delete_db_hook_called
    delete_db_hook_called = True
    a = my_threading_local.a
    if a.execute("select test(5, 6)").fetchone() != (5,):
        raise MyError
    return 1

def my_final(p):
    if my_threading_local.a.execute("select test(5, 6)").fetchone() != (5,):
        raise MyError
    return 1

def my_delete_db_hook(p):
    global delete_db_hook_called
    delete_db_hook_called = True
    return 1

delete_db_hook_called = False

