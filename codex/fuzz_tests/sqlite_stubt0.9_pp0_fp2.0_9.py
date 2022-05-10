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

ctypes.CDLL(ctypes.util.find_library("sqlite3"),
            ctypes.RTLD_GLOBAL).sqlite3_open(
                                        DB_URI,
                                        ctypes.byref(my_threading_local.a))
my_threading_local.a.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_URI), 1)
my_threading_local.a.sqlite3_progress_handler(ctypes.c_int(1), my_cb, None)
my_threading_local.a.sqlite3_busy_timeout(1000)

def insert_stuff():
    my_threading_local.a.execute("create table t(x, y)")
    my_threading_local.a.execute("insert into t values (1, 1)")
    my_threading_local.a.execute("insert into t values (1, 2)")
    my_threading_local.a.commit()

def select_stuff():
    cu = my
