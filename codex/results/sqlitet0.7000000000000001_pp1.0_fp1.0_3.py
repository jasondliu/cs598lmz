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

def my_del(p):
    del my_threading_local.a
    return 1


def test_pysqlite_threading():
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.set_authorizer(my_cb, my_del)
    my_conn = sqlite3.connect(DB_URI, uri=True)
    my_conn.execute("create table test (id integer)")
    my_conn.execute("insert into test (id) values (1)")
    my_conn.execute("insert into test (id) values (test(1, 2))")
    my_conn.execute("select test(id, 2) from test")
    del my_conn
