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

def pysqlite_finalize(p):
    del my_threading_local.a
    return 1

def pysqlite_init():
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.set_authorizer(my_cb)
    sqlite3.set_trace_callback(my_cb)
    sqlite3.set_progress_handler(my_cb, 100)
    sqlite3.set_update_hook(my_cb)
    sqlite3.set_profile(my_cb)
    sqlite3.set_rollback_hook(my_cb)

    # create a thread that uses the connection
    def run():
        conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        conn.execute("create table test (id integer primary key, value text)")
        conn.execute("insert into test (value) values (?)", ("foo",))
        conn.execute("select * from test")
        conn.commit()
        conn.close()

   
