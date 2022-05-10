import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as an argument.
# The function pointer is called with one integer argument.

# This is the function type the callback function must have.
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function to call.
func = lib.callback
func.argtypes = (CALLBACKFUNC, ctypes.c_int)
func.restype = ctypes.c_int

# This is the callback function.
@CALLBACKFUNC
def callback(arg):
    print("callback called with", arg)
    return arg * 2

# Call the function.
res = func(callback, 100)
print("callback returned", res)

# This is a function that takes a function pointer as an argument.
# The function pointer is called with one integer argument.

# This is the function type the callback function must have.
CALLBACK
