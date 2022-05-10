import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have the same signature as the
# CFUNCTYPE function we pass.

# The function is called 10 times, and the sum of the arguments
# passed is returned.

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(n):
    print('func', n)
    return n + 1

res = lib.sum_i(10, CMPFUNC(func))
if res != 55:
    raise RuntimeError("sum_i() returned %d, expected 55" % res)

# This is a function that takes a function pointer as argument.
# The function pointer must have the same signature as the
# CFUNCTYPE function we pass.

# The function is called 10 times, and the sum of the arguments
# passed is returned.

CMPFUNC = ctypes.CFUN
