import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have one integer argument, and returns
# an integer.

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function that we pass to the dll.

def callback(value):
    print("callback called with", value)
    return value + 1

# This is the function in the dll that takes the function pointer.

lib.set_callback.argtypes = CALLBACKFUNC,
lib.set_callback.restype = None

# Call the function in the dll.  The dll will call our callback function.

lib.set_callback(CALLBACKFUNC(callback))

# Call the function in the dll again.  The dll will call our callback
# function again.

lib.set_callback(CALLBACKFUNC(callback))

# Call
