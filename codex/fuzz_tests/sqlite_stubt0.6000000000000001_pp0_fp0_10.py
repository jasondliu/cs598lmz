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
    my_threading_local.a.execute("create table if not exists test(a, b)")
    my_threading_local.a.execute("insert into test values (1, 2)")
    return 1

def my_cb3(p):
    my_threading_local.a.execute("select * from test")
    return 1

def my_cb4(p):
    my_threading_local.a.execute("select test(a, b) from test")
    return 1

def main():
    print("Before loading sqlite3:")
    print("ctypes.util.find_library('sqlite3') = " + repr(ctypes.util.find_library("sqlite3")))
    print("ctypes.util.find_library('libsqlite3') = " + repr(ctypes.util.find_library("libsqlite3")))
    print("ctypes.util.find_library('libsqlite3.so') = " + repr(ctypes.util.find_library("
