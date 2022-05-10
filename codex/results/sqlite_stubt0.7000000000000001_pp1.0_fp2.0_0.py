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

def my_cb_dealloc(p):
    my_threading_local.a.close()
    my_threading_local.a = None
    return 1

sqlite3.sqlite_open = sqlite3.sqlite_open_v2
sqlite3.sqlite_set_authorizer = sqlite3.sqlite_set_authorizer
sqlite3.sqlite_config(sqlite3.SQLITE_CONFIG_URI, 1)
sqlite3.sqlite_config(sqlite3.SQLITE_CONFIG_AUTHORIZER, my_cb)
sqlite3.sqlite_config(sqlite3.SQLITE_CONFIG_AX_CONNECT, my_cb_dealloc)

a = sqlite3.connect(DB_URI, uri=True)
with a:
    a.execute("create table test(a,b,c)")
    a.execute("insert into test(a,b,c) values(1,2,3)")
    for r in a:
        print("%d %d %d
