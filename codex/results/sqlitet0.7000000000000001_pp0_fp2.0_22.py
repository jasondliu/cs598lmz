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

def my_cb_commit(p):
    my_threading_local.a.commit()
    return 1

def my_cb_rollback(p):
    my_threading_local.a.rollback()
    return 1

def my_cb_select(p):
    for row in my_threading_local.a.execute("select x from t"):
        pass
    return 1

def my_cb_insert(p):
    my_threading_local.a.execute("insert into t values (?)", ("test",))
    return 1

def my_cb_update(p):
    my_threading_local.a.execute("update t set x = test(x)")
    return 1

def my_cb_delete(p):
    my_threading_local.a.execute("delete from t")
    return 1

def my_cb_create(p):
    my_threading_local.a.execute("create table t (x)")
    return 1

def my_cb_destroy(p):
   
