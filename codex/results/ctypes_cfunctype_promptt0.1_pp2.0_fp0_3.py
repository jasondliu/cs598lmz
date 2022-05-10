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

lib.callit.argtypes = (CALLBACKFUNC,)
lib.callit.restype = ctypes.c_int

# This is the function to pass as argument.  It adds its argument
# to a counter, and returns the new value.

COUNTER = [0]
def callback(value):
    COUNTER[0] += value
    return COUNTER[0]

# Call the function in the dll.  The integer it returns is the
# sum of the values passed to the callback function.

result = lib.callit(CALLBACKFUNC(callback
