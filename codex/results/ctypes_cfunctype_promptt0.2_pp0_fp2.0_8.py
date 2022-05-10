import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a prototype
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
restype = ctypes.c_int
argtypes = (ctypes.c_int,)

func = prototype((b"_testfunc_prototype", lib), ((b"arg", ctypes.c_int),))
func.restype = restype
func.argtypes = argtypes

print(func(42))

# call a function without a prototype
func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)((b"_testfunc_no_prototype", lib))
print(func(42))

# call a function with a prototype, but no restype or argtypes
func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)((b"_testfunc_prototype", lib), ((b"arg", ctypes.c
