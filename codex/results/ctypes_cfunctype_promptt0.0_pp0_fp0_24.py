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
    return n * 2

f = CMPFUNC(func)

res = lib.call_function(10, f)
if res != 110:
    raise RuntimeError("Wrong result")

# Test passing None
try:
    lib.call_function(10, None)
except TypeError:
    pass
else:
    raise RuntimeError("passing None should not work")

# Test passing an integer
try:
    lib.call_function(10, 42)
except TypeError:
    pass

