import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

def func(arg):
    return arg * 2

FuncType = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

func_ptr = FuncType(func)

