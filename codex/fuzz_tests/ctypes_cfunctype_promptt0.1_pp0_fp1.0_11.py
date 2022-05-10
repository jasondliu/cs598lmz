import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointed to must take an integer argument, and return
# an integer.

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function that will be called from the C code.

def py_cmp_func(i):
    print("py_cmp_func", i)
    return -i

# This is the function that will be called from the C code.

def py_cmp_func_ex(i, j):
    print("py_cmp_func_ex", i, j)
    return -i

# This is the function that will be called from the C code.

def py_cmp_func_ex2(i, j, k):
    print("py_cmp_func_ex2", i, j, k)
    return -i

# This is the function that will be
