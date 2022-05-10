import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

def func(*args):
    return args

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)

lib.set_cmp_func.argtypes = (CMPFUNC,)
lib.set_cmp_func(cmp_func)

lib.qsort.argtypes = (ctypes.POINTER(ctypes.c_int),
                      ctypes.c_int, ctypes.c_int)

lib.qsort.restype = None

a = (ctypes.c_int * 5)(5, 4, 3, 2, 1)
lib.qsort(a, len(a), ctypes.sizeof(ctypes.c_int))

print(list(a))
