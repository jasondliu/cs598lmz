import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a simple function taking a float, returning a float
func = lib.my_function
func.argtypes = ctypes.c_float,
func.restype = ctypes.c_float

# This is a simple function taking a float, returning a float
func_p = lib.my_function_p
func_p.argtypes = ctypes.POINTER(ctypes.c_float),
func_p.restype = ctypes.POINTER(ctypes.c_float)

# This is a simple function taking a float, returning a float
func_pp = lib.my_function_pp
func_pp.argtypes = ctypes.POINTER(ctypes.POINTER(ctypes.c_float)),
func_pp.restype = ctypes.POINTER(ctypes.POINTER(ctypes.c_float))

# This is a simple function taking a float, returning a float
func_ppp = lib.my_function_ppp

