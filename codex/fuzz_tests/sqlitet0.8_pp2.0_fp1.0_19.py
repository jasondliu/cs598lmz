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

class SQLiteConnection:
    def __init__(self):
        # load sqlite library
        self.db_lib = None
        try:
            self.db_lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
        except:
            print "sqlite3 library not found"

    def create_connection(self):
        # create sqlite db in memory
        self.db_lib.sqlite3_open(DB_URI, ctypes.byref(self.db_obj))

    def create_test(self):
        self.db_lib.sqlite3_set_authorizer(self.db_obj, my_cb, None)

if __name__ == '__main__':
    SQLiteConnection()
