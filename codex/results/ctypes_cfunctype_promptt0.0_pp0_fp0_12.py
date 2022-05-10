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

res = lib.call_function(CMPFUNC(func), 10)
if res != 110:
    raise RuntimeError("Wrong result")

# Test passing None
try:
    lib.call_function(CMPFUNC(None), 10)
except TypeError:
    pass
else:
    raise RuntimeError("should have raised TypeError")

# Test passing an integer
try:
    lib.call_function(CMPFUNC(42), 10)
except TypeError:

