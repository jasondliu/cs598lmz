import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as an argument
# and calls it.
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function that is called by the function pointer.
def callback(arg):
    print("callback called with arg:", arg)
    return arg + 1

# Call the function with the function pointer.
res = lib.call_function(CALLBACK(callback), 1)
print("call_function returned:", res)

# This is a function that takes a function pointer as an argument
# and calls it.
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# This is the function that is called by the function pointer.
def callback(arg1, arg2):
    print("callback called with args:", arg1, arg2)
    return arg
