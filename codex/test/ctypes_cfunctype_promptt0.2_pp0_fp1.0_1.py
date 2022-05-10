import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have a simple signature: int()
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int)

# This is the function to call.
def callback():
    print("callback() called")
    return 42

# Call the function in lib, which takes a function pointer as argument.
