import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = CDLL(_ctypes_test.__file__)

def func(*args):
    print(args)

CMPFUNC = CFUNCTYPE(c_int, c_int, c_int)

cmp_func = CMPFUNC(func)

lib.qsort.argtypes = c_char_p, c_int, c_int, CMPFUNC
lib.qsort(b"12345", 5, 1, cmp_func)

# Test ctypes.PYFUNCTYPE

def func(*args):
    print(args)
    return args[-1]

CMPFUNC = PYFUNCTYPE(c_int, c_int, c_int)

cmp_func = CMPFUNC(func)

lib.qsort.argtypes = c_char_p, c_int, c_int, CMPFUNC
lib.qsort(b"12345", 5, 1, cmp_func)

# Test ctypes.WINFUNCTY
