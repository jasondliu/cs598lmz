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

    return 15

def cb(s, op, db_name, table_name, cookie):
    return my_cb

def main():
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a
    sqlite3.sqlite3_update_hook(a._conn, cb, None)

    a.execute("create table test(a int)").close()

    a.execute("insert into test values(1)")

    t = threading.Thread(target=a.execute("delete from test where 1=1").close)
    t.start()
    t.join()

    del my_threading_local.a
    del a

    ctypes.CDLL(ctypes.util.find_library('c')).prctl(15, 'test_child')

def my_test_fn(a, b):
    return a

def test_fn(a, b):
    t = my_
