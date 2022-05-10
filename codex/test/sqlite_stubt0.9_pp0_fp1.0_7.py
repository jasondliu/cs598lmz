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

def my_authorizer(action, arg1, arg2, dbname, trigger_or_view):
    print(action, arg1, arg2, dbname, trigger_or_view)

def my_progress():
    print("my_progress")
    return 0

def my_trace_cb(conn):
    print(conn)

def my_update_hook(conn, op, db, table, rowid):
    print(op, db, table, rowid)

libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.free.argtypes = [ctypes.c_void_p,]

def main():
    p = sqlite3.load_extension("pysqlite2.c", "sqlite3_pysqlite2_init")
    sqlite3.enable_callback_tracebacks(True)

    ret = sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_SERIALIZED)
    print("Config one:", ret)

    cone = sql
