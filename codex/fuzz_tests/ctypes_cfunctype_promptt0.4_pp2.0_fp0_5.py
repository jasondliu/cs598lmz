import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# Test with a function with a simple result type

# int function(int)
restype = ctypes.c_int
argtypes = (ctypes.c_int,)

func = lib.func
func.restype = restype
func.argtypes = argtypes

funcptr = ctypes.CFUNCTYPE(restype, argtypes[0])(("func", lib), argtypes)

for i in range(5):
    assert func(i) == i * 2
    assert funcptr(i) == i * 2

# Test with a function with a composite result type

# struct S function(int)
class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

restype = S
argtypes = (ctypes.c_int,)

func = lib.func_struct
func.restype = restype
func.argtypes = arg
