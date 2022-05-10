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

def my_cb_close(p):
    my_threading_local.a.close()
    my_threading_local.a = None

    return 1

def my_cb_open(p, fn):
    return SQLITE_OK

def my_cb_read(p, buf, amt):
    return 0

def my_cb_write(p, buf, amt):
    return 0

def my_cb_fsync(p):
    return SQLITE_OK

def my_cb_truncate(p, sz):
    return SQLITE_OK

def my_cb_file_size(p, sz):
    return SQLITE_OK

def my_cb_lock(p, lock):
    return SQLITE_OK

def my_cb_unlock(p, lock):
    return SQLITE_OK

def my_cb_check_reserved_lock(p):
    return 1

def my_cb_file_control(p, op, arg):
    return SQLITE_OK

def my_
