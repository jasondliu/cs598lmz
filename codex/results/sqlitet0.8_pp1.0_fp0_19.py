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

class CustomRegister:
    def sqlite3_custom_func(self, context, argc, argv):
        return 1

def my_function_callback(p, x, y):
    return x + y

def my_auth_callback(p, x, y, z):
    print(x, y, z)
    return x + y + z

def my_progress_callback(p):
    return 1

def my_update_handler(p, operation, database, table, rowid):
    print(operation, database, table, rowid)
    return 1

def my_trace_handler(p, sql):
    print(sql)
    return 1

def my_commit_handler(p):
    return 1

def my_rollback_handler(p):
    return 1

def main():
    sqlite3.enable_callback_tracebacks(True)

    ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_config(
        sqlite3.SQLITE_CONFIG_SING
