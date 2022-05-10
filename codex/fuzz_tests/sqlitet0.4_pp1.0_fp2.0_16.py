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
    return 1

def main():
    ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True).atexit(my_cb2)
    ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True).atexit(my_cb)

    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.execute("create table test (a, b)")
    a.execute("insert into test values (1, 2)")
    a.execute("insert into test values (3, 4)")
    a.execute("insert into test values (5, 6)")
    a.execute("insert into test values (7, 8)")
    a.execute("insert into test values (9, 10)")
    a.execute("insert into test values (11, 12)")
    a.execute("insert into test values (13, 14)")
   
