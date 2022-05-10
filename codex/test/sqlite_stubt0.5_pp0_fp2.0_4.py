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

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)
sqlite3.sqlite3_uri_boolean(1, True)
sqlite3.sqlite3_uri_int64(1, True)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_LOG, my_cb)

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

def test_fn(a, b):
    return a

a.create_function("test", 2, test_fn)

my_threading_local.a = a

a.execute("create table test (a text, b text)")
a.execute("insert into test values ('a', 'b')")
a.execute("insert into test values ('c', 'd')")
a.execute("insert into test values ('e', 'f')")

res = a.execute("select test(a, b) from test")

res = [x for x in res]


