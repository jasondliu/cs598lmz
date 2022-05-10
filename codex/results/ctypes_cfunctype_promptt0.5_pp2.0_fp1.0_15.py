import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

f = lib.my_function
f.argtypes = (ctypes.c_int, ctypes.c_int)
f.restype = ctypes.c_int

print f(1, 2) == 3

# Test ctypes.WINFUNCTYPE

f = lib.my_function_2
f.argtypes = (ctypes.c_int, ctypes.c_int)
f.restype = ctypes.c_int

print f(1, 2) == 3

# Test ctypes.PYFUNCTYPE

f = lib.my_function_3
f.argtypes = (ctypes.c_int, ctypes.c_int)
f.restype = ctypes.c_int

print f(1, 2) == 3
