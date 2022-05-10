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

