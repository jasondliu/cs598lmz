import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False)
# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=True)

# void func(int)
func = lib.func
func.argtypes = (ctypes.c_int,)
func.restype = None

# int func2(int)
func2 = lib.func2
func2.argtypes = (ctypes.c_int,)
func2.restype = ctypes.c_int

# void func3(int)
func3 = lib.func3
func3.argtypes = (ctypes.c_int,)
func3.restype = None
func3.errcheck = lambda result, func, args: None

# int func4(int)
func4 = lib.func4
func4.argtypes = (ctypes.c_int,)
func4.restype = ctypes.
