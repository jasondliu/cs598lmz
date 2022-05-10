import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import *
from ctypes.test import need_symbol

import _ctypes_test
lib = CDLL(_ctypes_test.__file__)

# This is a call-back function:
CMPFUNC = CFUNCTYPE(c_int, c_int, c_int)

def mycmp(a, b):
    return a - b

# This is the function taking the call-back:
qsort = lib.my_qsort
qsort.argtypes = [c_void_p, c_size_t, c_size_t, CMPFUNC]
qsort.restype = None

a = (c_int * 5)(5, 4, 3, 2, 1)
qsort(a, len(a), sizeof(c_int), CMPFUNC(mycmp))

for i in range(len(a)):
    assert a[i] == i + 1

# Test ctypes.PYFUNCTYPE

def py_mycmp(a, b):
    return a - b

#
