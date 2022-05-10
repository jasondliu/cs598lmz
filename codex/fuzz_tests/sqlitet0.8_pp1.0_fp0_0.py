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

def my_cb_second(p):
    a = my_threading_local.a
    return a.execute("SELECT test(1, 2)").fetchone()[0]

def main():
    libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"), use_errno = True)
    libsqlite3.sqlite3_threadsafe() == 2
    libsqlite3.sqlite3_open_v2(DB_URI.encode("ASCII"), ctypes.byref(my_threading_local.db), 0x40, "".encode("ASCII"))

    libsqlite3.sqlite3_key(my_threading_local.db, "password".encode("ASCII"))
    libsqlite3.sqlite3_exec(my_threading_local.db, "PRAGMA KDF_ITER=100000;".encode("ASCII"), None, None, None)

    libsqlite3.sqlite3_set_authorizer(my_threading_local.db
