import ctypes
# Test ctypes.CFUNCTYPE()

from ctypes import *
from _ctypes import funcptr

def check(restype, argtypes):
    func = CFUNCTYPE(restype, *argtypes)
    assert isinstance(func, funcptr)
    if len(argtypes) == 1:
        fn = func() # returns a function object
        assert isinstance(fn, funcptr)
        assert fn.__call__ == fn
    else:
        raises(TypeError, func)


check(c_int, [c_int])
check(c_int, [])
check(c_int, [c_int, c_int])

check(c_double, [c_double])
check(c_double, [c_double, c_double])
check(c_double, [c_int])
check(c_double, [c_int, c_int])
check(c_double, [])

check(c_longdouble, [c_longdouble])
check(c_longdouble, [c_longdouble, c_longdouble])
check(c_long
