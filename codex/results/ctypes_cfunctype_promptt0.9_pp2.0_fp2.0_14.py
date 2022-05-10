import ctypes
# Test ctypes.CFUNCTYPE
import sys


def test_cfunctype():
    int_f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
    def do_add(i):
        return i+1
    add_f = int_f(do_add)
    assert add_f(-1) == 0
    # Make sure GC doesn't crash
    del do_add
    import gc; gc.collect()


def test_cfunctype2():
    int_f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)
    def do_ptr(i):
        return ctypes.cast(i, ctypes.c_char_p).value
    ptr_f = int_f(do_ptr)
    assert ptr_f(b'testing') == b'testing'


def test_cfunctype3():
    int_f = ctypes.CFUNCTYPE(ctypes.c_int)
    def do_add():
        return 1
   
