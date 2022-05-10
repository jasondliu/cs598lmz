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

@WINFUNCTYPE(c_int, c_int)
def func(a):
    return a + 1

# Test ctypes.FUNCTYPE()

@FUNCTYPE(c_int, c_int)
def func(a):
    return a + 1


# Test ctypes.addressof()

def func():
    pass

addressof(func)

# Test ctypes.byref()

def func():
    pass

byref(func)

# Test ctypes.cdll.LoadLibrary()

from ctypes import *
try:
    cdll.
