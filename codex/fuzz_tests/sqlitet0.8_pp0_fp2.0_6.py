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

def main():
    l = ctypes.util.find_library("sqlite3")
    assert l
    lib = ctypes.CDLL(l)

    cb = lib.sqlite3_set_authorizer
    cb.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
    cb.restype = lib.sqlite3_set_authorizer
    my_cb_p = ctypes.CFUNCTYPE(None, ctypes.c_void_p)(my_cb)

    db = sqlite3.connect(DB_URI)
    r = db.execute("""
        PRAGMA recursive_triggers=ON;
        CREATE TABLE a (b);
        CREATE TABLE b (c);
        INSERT INTO b VALUES (45);
        CREATE TRIGGER ai AFTER INSERT ON b
            BEGIN
                INSERT INTO a
