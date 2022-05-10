import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have the signature:
# int func(double)
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_double)

# This is the function to pass to the dll.
def callbackfunc(value):
    print('callbackfunc called with', value)
    return int(value * 2)

# Call the dll function.
res = lib.set_callback(CALLBACKFUNC(callbackfunc))
print('set_callback returned', res)

# Call the dll function.
res = lib.call_callback(2.5)
print('call_callback returned', res)
