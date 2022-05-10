import ctypes
# Test ctypes.CFUNCTYPE()

##stdcall = ctypes.WINFUNCTYPE(ctypes.c_int)
##stdcall(lambda:1)

# Works in Python 2.4 and above

# Test ctypes.PYFUNCTYPE()

from ctypes import *

@CFUNCTYPE(c_int, c_int)
def func(a):
    return a + 1

# Test ctypes.WINFUNCTYPE()

