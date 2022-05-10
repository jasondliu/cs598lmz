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

print(func("hello %s\n", "world"))

# a function with a variable number of arguments
# and a non-standard calling convention
func = lib.my_strlen
func.argtypes = ctypes.c_char_p,
func.restype = ctypes.c_int
func.calltype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)

print(func("hello world"))

# a function with a variable number of arguments
# and a non-standard calling convention
func = lib.
