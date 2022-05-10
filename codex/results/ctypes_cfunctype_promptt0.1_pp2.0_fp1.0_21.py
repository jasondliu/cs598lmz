import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have the same signature as the
# CFUNCTYPE function pointer type we create.

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def py_cmp_func(a, b):
    print("py_cmp_func", a, b)
    return a - b

cmp_func = CMPFUNC(py_cmp_func)

lib.my_qsort.argtypes = (ctypes.c_void_p, ctypes.c_int, ctypes.c_int, CMPFUNC)
lib.my_qsort.restype = ctypes.c_int

a = (ctypes.c_int * 5)(5, 4, 3, 2, 1)
lib.my_qsort(a, len(a), ctypes.sizeof
