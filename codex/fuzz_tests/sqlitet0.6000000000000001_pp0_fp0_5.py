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

def my_cb_step(p, a, b):
    return 1

def my_cb_final(p):
    return 1

def my_cb_list(p, a):
    return 1

def my_cb_value(p, a, b, c):
    return 1

if __name__ == "__main__":
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.set_authorizer(my_cb)
    sqlite3.complete_statement("")
    sqlite3.aggregate_count("")
    sqlite3.aggregate_count("")
    sqlite3.aggregate_count("")
    sqlite3.aggregate_count("")
    sqlite3.aggregate_count("")
    sqlite3.aggregate_count("")
    sqlite3.aggregate_count("")
    sqlite3.aggregate_count("")
    sqlite3.aggregate_count("")
    sqlite3.aggregate_count("")
    sqlite3.aggregate_count
