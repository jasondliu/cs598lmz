import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# int func(int)
func = lib.func
func.argtypes = (ctypes.c_int,)
func.restype = ctypes.c_int

print func(1)

# int func2(int, int)
func2 = lib.func2
func2.argtypes = (ctypes.c_int, ctypes.c_int)
func2.restype = ctypes.c_int

print func2(1, 2)

# int func3(int, int, int)
func3 = lib.func3
func3.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_int)
func3.restype = ctypes.c_int

print func3(1, 2, 3)

# int func4(int, int, int, int)
func4 = lib.func4
func4.argtypes = (ctypes.c_int, ctypes.c
