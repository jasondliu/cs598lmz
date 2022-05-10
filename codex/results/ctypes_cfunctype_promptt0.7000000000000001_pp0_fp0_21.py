import ctypes
# Test ctypes.CFUNCTYPE
#
# Issues:
#  - PyPy crashes
#  - PyPy 1.9 misses the function name
# TODO:
#  - test Python 2.x

import _ctypes
from ctypes import *

def test(f, name):
    assert f.__name__ == name
    assert f.__class__ == CFUNCTYPE(c_int)
    assert f.__doc__ is None
    assert f.__dict__ == {}
    assert f.argtypes is None
    assert f.restype is c_int
    assert f(0) == 1
    f.argtypes = None
    f.restype = None
    assert f(0) == 1

test(CFUNCTYPE(c_int, c_int), "CFUNCTYPE(c_int, c_int)")
test(CFUNCTYPE(c_int)(lambda x: 1), "lambda")
test(CFUNCTYPE(c_int, c_int)(lambda x: 1), "lambda")

try:
    class MyCFunctionType
