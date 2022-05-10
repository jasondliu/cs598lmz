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

def my_init():
    lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    lib.sqlite3_yt_init(my_cb)


my_init()

try:
    c = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    c.executescript("""
    create table my_table(a, b, c);
    insert into my_table(a, b, c) values(1,2,3);
    insert into my_table(a, b, c) values(3,2,1);
    insert into my_table(a, b, c) values(1,4,4);
    insert into my_table(a, b, c) values(4,4,4);
    """)
    c.commit()

    print((c.execute("select test(a, b) from my_table where b==2").fetchall()))
    print((c.execute("select test(a, b) from my_table where c
