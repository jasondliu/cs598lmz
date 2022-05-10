import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a simple test for ctypes.CFUNCTYPE.
#
# The test function takes a function pointer as first argument.
# The function pointer is called with three integers as arguments, and
# the return value of the function pointer is returned by the test
# function.

# The function pointer type is defined like this:
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)

# This is the function called by the test function:
def func(a, b, c):
    print("func", a, b, c)
    return a + b + c

# This is the function pointer we pass to the test function:
f = CMPFUNC(func)

# Call the test function:
