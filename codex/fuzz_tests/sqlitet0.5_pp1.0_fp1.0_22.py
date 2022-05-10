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

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)
my_cb_p = sqlite3.sqlite3_set_authorizer(my_cb, 0)

def authorize_cb(p, action, arg1, arg2, dbname, source):
    return 1

def test_thread():
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.set_authorizer(authorize_cb)
    conn.execute("select test(1, 2)")
    conn.close()

threads = [threading.Thread(target=test_thread) for i in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

sqlite3.sqlite3_set_authorizer(my_cb_p, 0)
