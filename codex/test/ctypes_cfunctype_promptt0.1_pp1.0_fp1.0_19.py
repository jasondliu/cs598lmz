import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointed to must take an integer argument, and return
# an integer.

# The prototype of the function passed to the test function is:
# int func(int)

FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function that will be passed to the test function.
# It must have the prototype: int func(int)

def py_func(arg):
    return arg * arg

# The test function takes a function pointer as first argument,
# and an integer as second argument.  It calls the function pointer
# with the integer argument, and returns the result.

# The prototype of the test function is:
# int test_func(int (*func)(int), int arg)

