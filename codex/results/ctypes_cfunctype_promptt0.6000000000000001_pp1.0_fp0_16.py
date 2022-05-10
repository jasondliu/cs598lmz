import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import *
import _ctypes_test

callback = CFUNCTYPE(c_int, c_int, c_int)

def mycallback(a, b):
    print(a, b)
    return a + b

cbfunc = callback(mycallback)

_ctypes_test.set_callback(cbfunc)

if _ctypes_test.call_callback(2, 3) != 5:
    print('CFUNCTYPE callback test failed!')

# Test ctypes.PYFUNCTYPE
from ctypes import *

PYFUNCTYPE = CFUNCTYPE

class Bar(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int)]

class Foo(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int),
                ("c", Bar),
                ("d", c_char_p)]

def pyfunc(a, b, c, d):
    print(a, b, c,
