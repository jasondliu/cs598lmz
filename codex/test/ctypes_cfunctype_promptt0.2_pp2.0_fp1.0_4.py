import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# Prototype a function with a callback
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Define a callback function
@prototype
def callback(i):
    print("callback", i)
    return i + 1

# Call the function with the callback
