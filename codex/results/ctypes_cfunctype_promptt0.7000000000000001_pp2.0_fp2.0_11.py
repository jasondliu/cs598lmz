import ctypes
# Test ctypes.CFUNCTYPE
import _ctypes_test

lib = CDLL(_ctypes_test.__file__)
call_int = lib.call_int
call_int.argtypes = (CFUNCTYPE(c_int),)
call_int.restype = c_int

@CFUNCTYPE(c_int)
def func(*args):
    return len(args)

assert call_int(func) == 0

@CFUNCTYPE(c_int, c_int)
def func(arg):
    return arg

assert call_int(func) == 42

@CFUNCTYPE(c_int, c_int, c_int)
def func(arg1, arg2):
    return arg1 + arg2

assert call_int(func) == 42

@CFUNCTYPE(c_int, c_int, c_int, c_int, c_int, c_int, c_int)
def func(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
    return arg
