import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have the signature:
# int func(int)
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function to pass to the dll.
def callback(i):
    print("callback", i)
    return i + 42

# Call the dll function.  The integer it returns is the result of
# calling the callback function.
