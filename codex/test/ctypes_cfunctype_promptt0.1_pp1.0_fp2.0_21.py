import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointed to must take an integer argument and return
# an integer.

# The prototype of the function pointer is:
# int func(int)

FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function that will be passed to the dll.

@FUNC
def func(arg):
    print("func", arg)
    return arg * 2

# Call the dll function.  It returns the value we passed in.

