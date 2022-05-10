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

    if not a:
        return 1

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    return 1

def main():
    c_lib_path = ctypes.util.find_library("c")
    c_lib = ctypes.CDLL(c_lib_path)

    print "Address of 'main': ", hex(c_lib.main)

    main_ptr = ctypes.c_void_p.from_address(c_lib.main)

    print "Address of 'main' via c_void_p.from_address: ", main_ptr.value

    my_cb_addr = ctypes.addressof(my_cb)
    my_cb2_addr = ctypes.addressof(my_cb2)

    print "Address of 'my_cb': ", hex(my_cb_addr)
    print "Address of 'my_cb2': ", hex(my_
