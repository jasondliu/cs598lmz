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

def my_cb_vt(vt):
    my_threading_local.a.close()

    return 0

def my_cb_p(p):
    return 1

def my_cb_p_vt(vt):
    my_threading_local.a.close()

    return 0

def my_cb_tn(tn):
    return 1

def my_cb_vn(vn):
    return 1

def my_cb_vn_tn(tn):
    return 1

def my_cb_vn_tn_p(p):
    return 1

def my_cb_vn_tn_p_vt(vt):
    return 0

def my_cb_vn_tn_p_vt_p(p):
    return 1

def my_cb_vn_tn_p_vt_p_vt(vt):
    return 0

def my_cb_vn_tn_p_vt_p_vt_p(p):
    return 1

def my_cb_vn_tn_
