import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# test a simple function call

# int func(int)
func = lib.func
func.restype = ctypes.c_int
func.argtypes = (ctypes.c_int,)

# int func2(int, int)
func2 = lib.func2
func2.restype = ctypes.c_int
func2.argtypes = (ctypes.c_int, ctypes.c_int)

# int func3(int, int, int)
func3 = lib.func3
func3.restype = ctypes.c_int
func3.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_int)

# int func4(int, int, int, int)
func4 = lib.func4
func4.restype = ctypes.c_int
func4.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_
