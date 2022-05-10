import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# Calling conventions.
cdecl = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
stdcall = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# argtypes and restype set.
@stdcall(ctypes.c_int, ctypes.c_int)
def func(*args):
    print(args)
    return args[-1]

# No argtypes set.
@stdcall()
def func_noargtype(arg):
    print(arg)
    return arg

# No restype set.
@stdcall(ctypes.c_int, restype=None)
def func_norestype(arg):
    print(arg)

# No argtypes and restype set.
@stdcall()
def func_noargtype_norestype(arg):
    print(arg)

# argtypes set, restype
