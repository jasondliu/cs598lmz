import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function taking a function pointer as argument
# and calling it.

# The function pointer takes an integer argument and returns
# an integer.

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(arg):
    print("callback called with", arg)
    return arg + 42

# The callback function is passed to the test function
# as argument.

