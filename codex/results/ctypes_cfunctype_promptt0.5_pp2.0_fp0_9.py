import ctypes
# Test ctypes.CFUNCTYPE

import ctypes
from ctypes import *

#
# This test is not complete, it just checks that CFUNCTYPE can be used
# to create a function pointer, and that it can be passed to a C function.
#

libc = CDLL(ctypes.util.find_library("c"))

# callbacks
CMPFUNC = CFUNCTYPE(c_int, c_void_p, c_void_p)

# prototypes
libc.qsort.argtypes = [c_void_p, c_size_t, c_size_t, CMPFUNC]

# test data
data = (c_int * 5)(5, 1, 7, 33, 22)

# test code
def py_cmp(a, b):
    print("py_cmp", a, b)
    aa = cast(a, POINTER(c_int))
    bb = cast(b, POINTER(c_int))
    return aa.contents.value - bb.contents.value

buf = cast(data,
