import ctypes
# Test ctypes.CFUNCTYPE()

# This function takes a function pointer as first argument
# and returns the same pointer.

# The function pointer must accept an integer argument and
# return an integer result.

# The function pointer must be callable from C.

import sys
import ctypes
from ctypes import *

if sys.platform == "win32":
    import _ctypes_test
    dll = CDLL(_ctypes_test.__file__)
    func = dll._testfunc_callback
else:
    func = CDLL(None).testfunc_callback

CMPFUNC = CFUNCTYPE(c_int, c_int)

def py_cmp_func(i):
    print("py_cmp_func", i)
    return i

cmp_func = CMPFUNC(py_cmp_func)

res = func(cmp_func, 1)
if res != 1:
    raise Exception("Unexpected result")
