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

def test_func(p):
    return 1

def test_step(p, a, b, c):
    return 1

def test_final(p):
    return 1

def test_destroy(p):
    return 1

def test_auth(p, a, b, c):
    return 1

def test_trace(p, a):
    return 1

def test_profile(p, a, b):
    return 1

def test_progress(p):
    return 1

def test_update(p, a, b, c, d):
    return 1

def test_commit(p):
    return 1

def test_rollback(p):
    return 1

def test_wal_hook(p, a, b, c):
    return 1

def test_vfs_find(p, a):
    return 1

def test_vfs_register(p):
    return 1

def test_vfs_unregister(p, a):
    return 1

def test_mutex_enter(p
