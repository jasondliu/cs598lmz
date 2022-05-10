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

libc = ctypes.CDLL(ctypes.util.find_library("c"))

libc.setuid(100)
# Set thread callback!
sqlite3.enable_shared_cache(True)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_SERVER_CALLBACK, my_cb)

a = sqlite3.connect(":memory:", uri=False)

print "connect success"

# Callback must be called before!
b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

print "sub connect success"

cur = b.cursor()

try:
    cur.execute(
        "create table test(id integer primary key autoincrement, nid integer);"
    )

    cur.execute(
        "create table test2(id integer primary key autoincrement, nid integer);"
    )

    cur.execute(
        "create table test3(id integer primary key autoincrement, nid integer);"
    )
