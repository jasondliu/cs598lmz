import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointed to must take an integer argument, and return
# an integer.

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

@CMPFUNC
def py_cmp_func(i):
    print('py_cmp_func', i)
    return -i

lib.set_cmp_func.argtypes = CMPFUNC,
lib.set_cmp_func.restype = None

lib.sort.argtypes = ctypes.c_int, ctypes.POINTER(ctypes.c_int)
lib.sort.restype = None

lib.set_cmp_func(py_cmp_func)

a = (ctypes.c_int * 5)(5, 4, 3, 2, 1)
lib.sort(5, a)
print([a[i] for i in range(
