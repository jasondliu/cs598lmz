import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This function is declared as:
# int func(int (*)(int))
func = lib.func
func.argtypes = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int),
func.restype = ctypes.c_int

# This function is declared as:
# int func2(int (*)(int, int), int)
func2 = lib.func2
func2.argtypes = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int), ctypes.c_int
func2.restype = ctypes.c_int

# This function is declared as:
# int func3(int (*)(int, int, int), int, int)
func3 = lib.func3
func3.argtypes = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, c
