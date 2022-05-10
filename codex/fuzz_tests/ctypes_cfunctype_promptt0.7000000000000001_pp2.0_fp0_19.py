import ctypes
# Test ctypes.CFUNCTYPE and .from_param

import ctypes
from ctypes import *

callback = CFUNCTYPE(c_int, c_int, c_int)

@callback
def func(a, b):
    return a + b

def test(f):
    py.test.raises(ValueError, 'f.from_param(None)')
    f.from_param(f)

test(callback)

# test with a class containing a CFUNCTYPE attribute
class X(object):
    func = CFUNCTYPE(c_int, c_int, c_int)

@X.func
def func2(a, b):
    return a + b

test(X.func)
