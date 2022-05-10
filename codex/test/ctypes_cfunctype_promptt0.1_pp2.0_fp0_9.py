import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument
# and calls it.
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function that is called by the function pointer.
def callback(arg):
    print("callback called with argument", arg)
    return arg + 1

# This is the function that takes a function pointer as argument.
# It returns the result of calling the function pointer.
