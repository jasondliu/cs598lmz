import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def _make_func(f):
    return FUNTYPE(f)

def _make_func_ptr(f):
    return ctypes.cast(_make_func(f), ctypes.c_void_p).value

def _make_func_ptr_ptr(f):
    return ctypes.cast(_make_func(f), ctypes.POINTER(ctypes.c_void_p)).contents

class MyClass(object):
    def __init__(self):
        self.x = 0

    def f(self, x):
        self.x = x
        return x

def f(x):
    return x

def test_make_func():
    assert _make_func(f)(1.5) == 1.5
    assert _make_func_ptr(f)(1.5) == 1.5
    assert _make_func_ptr_ptr(f).value(1.5) == 1.5

def test_make_func_with_self():
    obj
