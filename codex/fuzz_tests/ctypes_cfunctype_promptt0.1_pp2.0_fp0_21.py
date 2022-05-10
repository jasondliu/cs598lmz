import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have the same signature as the
# CFUNCTYPE function we pass.

# The function is called 10 times, and the sum of the return values
# should be 55.

CALLCONV = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

@CALLCONV
def func(i):
    print('func', i)
    return i

result = lib.call_function(10, func)
if result != 55:
    raise Exception("%d != 55" % result)

# Test ctypes.WINFUNCTYPE

if ctypes.sizeof(ctypes.c_void_p) == ctypes.sizeof(ctypes.c_ulong):
    WINFUNCTYPE = ctypes.WINFUNCTYPE
else:
    WINFUNCTYPE = ctypes.WINFUN
