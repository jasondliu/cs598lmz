import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a simple prototype
func = lib.my_function
func.argtypes = None, ctypes.c_int
func.restype = ctypes.c_int
assert func(42) == 42

# call a function with a function pointer argument
func = lib.my_function_caller
func.argtypes = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int), ctypes.c_int
func.restype = ctypes.c_int
assert func(func, 42) == 42

# call a function with a function pointer argument
func = lib.my_function_caller
func.argtypes = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int), ctypes.c_int
func.restype = ctypes.c_int
assert func(func, 42) == 42

# call a function with a function pointer argument
func = lib.my_
