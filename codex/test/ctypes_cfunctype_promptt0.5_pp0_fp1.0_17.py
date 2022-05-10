import ctypes
# Test ctypes.CFUNCTYPE with only one parameter
# This used to crash on 64-bit platforms because the generated
# wrapper function had a different signature than the original
# function.

def func(a):
    return a

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

f = prototype(func)

