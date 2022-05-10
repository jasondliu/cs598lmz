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
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.set_progress_handler(my_cb, 1)
    a.execute("create table test (a)")
    a.execute("insert into test values (1)")
    a.execute("insert into test values (2)")
    a.execute("insert into test values (3)")
    a.execute("insert into test values (4)")
    a.execute("insert into test values (5)")
    a.execute("insert into test values (6)")
    a.execute("insert into test values (7)")
    a.execute("insert into test values (8)")
    a.execute("insert into test values (9)")
    a.execute("insert into test values (10)")
    a.execute("insert into test values (11)")
    a.execute("insert into test values (12)")
    a.execute("insert into test values (13)")
    a.execute("insert into test values (14
