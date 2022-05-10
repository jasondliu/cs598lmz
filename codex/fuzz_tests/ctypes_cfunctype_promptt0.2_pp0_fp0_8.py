import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have one integer argument, and returns
# an integer.

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function to call.  It takes a function pointer as
# argument, and calls it.

lib.pass_in_function.argtypes = (CALLBACKFUNC,)
lib.pass_in_function.restype = ctypes.c_int

# This is the function to pass in.  It takes an integer argument,
# and returns the argument incremented by one.

def callback(arg):
    print("callback called with", arg)
    return arg + 1

# This is the function to call.  It takes a function pointer as
# argument, and calls it.

result = lib.pass_in_function(CALLBACKFUNC(callback))
print("result
