import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument
# and calls it.
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function to call.
def callback(arg):
    print("callback called with argument", arg)
    return arg + 1

# This is the function that takes a function pointer as argument
# and calls it.
lib.callit(CALLBACK(callback))

# This is a function that takes a function pointer as argument
# and calls it.
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# This is the function to call.
def callback(arg1, arg2):
    print("callback called with arguments", arg1, arg2)
    return arg1 + arg2

# This is the function that takes a function pointer as argument
# and
