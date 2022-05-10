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

lib.call_cmp_func.argtypes = ctypes.c_int,
lib.call_cmp_func.restype = ctypes.c_int

lib.set_cmp_func(py_cmp_func)
print(lib.call_cmp_func(42))

# This is a function that takes a function pointer as argument.
# The function pointed to must take an integer argument, and return
# a
