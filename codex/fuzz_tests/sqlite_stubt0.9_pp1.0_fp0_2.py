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
    del my_threading_local.a
    return 1

sqlite3.enable_shared_cache(True)

libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.malloc.restype = ctypes.c_void_p
libc.malloc.argtypes = [ctypes.c_size_t]

p = sqlite3.sqlite3_preupdate_hook(my_cb, None)
p2 = sqlite3.sqlite3_commit_hook(my_cb2, None)

db_conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
try:
    db_conn.execute("create table t1(id INT PRIMARY KEY)")
    db_conn.execute("insert into t1 values(1)")
    db_conn.execute("insert into t1 values(2)")
    db_conn.execute("update t1 set id = test(2334, 3) where id
