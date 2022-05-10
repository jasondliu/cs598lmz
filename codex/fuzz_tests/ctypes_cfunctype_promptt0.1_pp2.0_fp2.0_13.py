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

lib.pass_int_callback.argtypes = (CALLBACKFUNC,)
lib.pass_int_callback.restype = ctypes.c_int

# This is the function to pass as argument.

@CALLBACKFUNC
def callbackfunc(value):
    print('callbackfunc called with value', value)
    return value + 1

# Call the function with our callback as argument.

result = lib.pass_int_callback(callbackfunc)
print('pass_int_callback returned', result)

# This is a function that takes a function pointer as argument.
#
