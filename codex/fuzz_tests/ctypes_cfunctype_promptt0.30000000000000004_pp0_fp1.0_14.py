import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a prototype
# int func(int)
func = lib.func
func.restype = ctypes.c_int
func.argtypes = (ctypes.c_int,)

print func(42)

# call a function with a prototype
# int func2(int, int)
func2 = lib.func2
func2.restype = ctypes.c_int
func2.argtypes = (ctypes.c_int, ctypes.c_int)

print func2(42, 43)

# call a function with a prototype
# int func3(int, int, int)
func3 = lib.func3
func3.restype = ctypes.c_int
func3.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_int)

print func3(42, 43, 44)

# call a function with a prototype
# int func4(int, int
