import ctypes
# Test ctypes.CFUNCTYPE on a simple function

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# a simple integer-returning function
func = lib.func
func.restype = ctypes.c_int
func.argtypes = None

print(func())

# a function with a structure argument
func.restype = ctypes.c_int
func.argtypes = ctypes.c_int,

print(func(42))

# a function with a structure pointer argument
func.restype = ctypes.c_int
func.argtypes = ctypes.POINTER(ctypes.c_int),

print(func(ctypes.pointer(ctypes.c_int(42))))

# a function with a structure pointer argument
func.restype = ctypes.c_int
func.argtypes = ctypes.POINTER(ctypes.c_int),

print(func(ctypes.pointer(ctypes.c_int(42))))

# a function with a structure pointer argument
func.restype = ctypes.
