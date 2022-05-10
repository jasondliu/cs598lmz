import ctypes
# Test ctypes.CFUNCTYPE.
from ctypes import *
import sys

# test whether we are using the Microsoft C runtime, or not
# (the test is quite heuristic...)

do_msvc_test = True
for c in cdll.msvcrt._handle.__str__():
    if not c in "0123456789":
        do_msvc_test = False
        break

# XXX explain more!

if do_msvc_test:
    if sizeof(c_int) == sizeof(c_void_p):
        FUNC_FLAGS = WINFUNCTYPE
    else:
        FUNC_FLAGS = CFUNCTYPE
else:
    FUNC_FLAGS = CFUNCTYPE

def func(*args):
    for i in args:
        assert isinstance(i, int)
    return len(args)

# calling with different amount of parameters.
# returns the number of parameters as result
MyFuncType = FUNC_FLAGS(c_int, c_int)
f = MyFuncType(func)

assert c_
