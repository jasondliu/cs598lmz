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

def my_cb2(p):
    my_threading_local.a.close()
    my_threading_local.a = None
    return 1

def main():
    sqlite3.enable_callback_tracebacks(True)
    cb_func = sqlite3.sqlite3_progress_handler(my_cb, 1)
    cb_func2 = sqlite3.sqlite3_progress_handler(my_cb2, 1)
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.execute("create table test (a int)")
    conn.execute("insert into test values (1)")
    conn.execute("insert into test values (2)")
    conn.execute("insert into test values (3)")
    conn.execute("insert into test values (4)")
    conn.execute("insert into test values (5)")
    conn.execute("insert into test values (6)")
    conn.execute("insert into test values (7)")
    conn.execute
