import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# A function taking a callback as first argument
func = lib.callbackfunc
func.argtypes = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int), ctypes.c_int
func.restype = ctypes.c_int

# The callback
@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def my_callback(value):
    print('my_callback called with value %d' % value)
    return value + 1

# Call the function
print(func(my_callback, 1))

# Test ctypes.WINFUNCTYPE

# A function taking a callback as first argument
func = lib.callbackfunc
func.argtypes = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int), ctypes.c_int
func.restype = ctypes.c_int

# The callback
@ctypes
