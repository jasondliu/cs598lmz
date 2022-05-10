import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# a function pointer
Callable = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# a function taking a function pointer
func = lib.pointer_33
func.argtypes = [Callable]
func.restype = ctypes.c_int

# a function taking a function pointer, and returning a function pointer
func2 = lib.pointer_33_33
func2.argtypes = [Callable]
func2.restype = Callable

# a function taking a function pointer, returning a function pointer,
# and taking a function pointer
func3 = lib.pointer_33_33_33
func3.argtypes = [Callable]
func3.restype = Callable

# a function taking a function pointer, returning a function pointer,
# taking a function pointer, and returning a function pointer
func4 = lib.pointer_33_33_33_33
func4.argtypes = [Callable]
func
