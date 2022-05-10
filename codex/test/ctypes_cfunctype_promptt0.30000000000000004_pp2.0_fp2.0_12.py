import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# a simple function
func = lib.my_sqrt
func.argtypes = ctypes.c_double,
func.restype = ctypes.c_double

print(func(2))

# a function with a variable number of arguments
func = lib.printf
func.argtypes = ctypes.c_char_p,
func.restype = ctypes.c_int

