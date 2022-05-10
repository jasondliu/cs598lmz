import ctypes
# Test ctypes.CFUNCTYPE for multiple values
from ctypes import *

def check(restype, argtypes, *args):
    func = CFUNCTYPE(restype, *argtypes)(lambda *args: args)
    result = func(*args)
    print(result)
    assert result == args

if sizeof(c_int) == sizeof(c_void_p):
    check(c_int, [c_int], 123)
    check(c_int, [c_void_p], 123)
    check(c_int, [c_int, c_double], 123, 1.23)
    check(c_int, [c_void_p, c_double], 123, 1.23)
    check(c_void_p, [c_int, c_double], 123, 1.23)
    check(c_int, [c_int, c_int], 123, 456)
    check(c_int, [c_int, c_void_p], 123, 456)
