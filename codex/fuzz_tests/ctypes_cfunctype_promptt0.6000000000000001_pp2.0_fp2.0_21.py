import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
#
# This test is adapted from the ctypes tutorial:
# http://docs.python.org/library/ctypes.html#tutorials-and-howtos

import os, sys
from ctypes import *
libc = CDLL(os.path.join(os.getcwd(), "libc.so"))

# prototype of the C function
CMPFUNC = CFUNCTYPE(c_int, c_int, c_int)

# the C function
def py_cmp_func(a, b):
    print "py_cmp_func", a, b
    return a - b

# convert the Python function into C function
cmp_func = CMPFUNC(py_cmp_func)

# call the C qsort function
# qsort is defined in the standard C library, here we use the one
# provided by libc.so
libc.qsort(c_int(0), c_int(0), c_int(0), cmp_func)

# the
