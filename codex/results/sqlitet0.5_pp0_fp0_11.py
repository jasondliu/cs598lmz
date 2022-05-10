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
    a = my_threading_local.a

    a.execute("select test(?, ?)", (1, 2))
    return 1

def main():
    sqlite3.threadsafety = 1

    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.execute("create table foo (id integer primary key, name text)")
    a.execute("insert into foo (id, name) values (?, ?)", (1, "foo"))
    a.commit()

    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_initialize()

    sqlite3.enable_callback_tracebacks(True)

    lib.sqlite3_busy_handler(a.dbapi_connection, my_cb, None)
    lib.sqlite3_busy_handler(a.dbapi_connection, my_cb2, None)

    lib.sqlite3_shutdown()

if __name__ == "
