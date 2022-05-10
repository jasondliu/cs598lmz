import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a simple prototype
func = lib.my_sqrt
func.argtypes = ctypes.c_double,
func.restype = ctypes.c_double

print(func(2.0))

# call a function with a complex prototype
func = lib.my_strchr
func.argtypes = ctypes.c_char_p, ctypes.c_char
func.restype = ctypes.c_char_p

print(func(b"abcdef", b"d"))

# call a function with a C++ name mangling
func = lib.my_sqrt
func.argtypes = ctypes.c_double,
func.restype = ctypes.c_double

print(func(2.0))

# call a function with a C++ name mangling
func = lib.my_strchr
func.argtypes = ctypes.c_char_p, ctypes.c_char
