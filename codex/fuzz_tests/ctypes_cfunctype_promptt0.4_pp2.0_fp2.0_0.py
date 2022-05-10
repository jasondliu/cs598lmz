import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

restype = ctypes.c_int
argtypes = (ctypes.c_int,)

# Test with prototype
func = prototype((b"_ctypes_testfunc_p", lib), ((1,),))
assert func(1) == 3

# Test with restype and argtypes
func = prototype((b"_ctypes_testfunc_p", lib), (argtypes, restype))
assert func(1) == 3

# Test with restype and argtypes, but without prototype
func = prototype((b"_ctypes_testfunc_p", lib))
func.argtypes = argtypes
func.restype = restype
assert func(1) == 3

# Test with restype and argtypes, but without prototype
func = prototype((b"_ctypes_testfunc_p", lib))
func.argtypes = argtypes
func
