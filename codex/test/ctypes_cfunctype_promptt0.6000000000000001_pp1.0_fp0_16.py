import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import *
import _ctypes_test

callback = CFUNCTYPE(c_int, c_int, c_int)

def mycallback(a, b):
    print(a, b)
    return a + b

cbfunc = callback(mycallback)

