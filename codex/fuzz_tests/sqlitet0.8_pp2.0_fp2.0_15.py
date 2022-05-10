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

def get_me_a_conn():
    return my_threading_local.a

orig_sqlite_open = sqlite3.connect
def my_sqlite_open(one, two):
    if one == ":memory:":
        one = DB_URI
    return orig_sqlite_open(one, two)

sqlite3.connect = my_sqlite_open

d = sqlite3.connect(":memory:")

d.executescript("""
    create table test (one text);
    insert into test values ('test');
    """)

d.create_function("my_cb", 0, my_cb)

d.commit()

d.close()

d = sqlite3.connect(":memory:", uri=True, factory=deleting_conn)

d.executescript("""
    create table test (one text);
    insert into test values ('test');
    """)

d.create_function("get_me_a_conn", 0, get_me_a_conn)


