import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument
# and calls it.
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# The function to be called.
def func(arg):
    print("called with", arg)
    return arg + 1

# Callback function wrapper
callback = CALLBACK(func)

# Call the function that takes a function pointer
