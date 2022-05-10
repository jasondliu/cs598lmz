import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointed to must take an integer argument and return
# an integer.

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function to be passed to the dll.

def callback(value):
    print("callback called with", value)
    return value + 1

# Call the dll function, passing callback.

lib.set_callback(CALLBACKFUNC(callback))

# Call the dll function, which will call the callback.

lib.call_callback(5)
