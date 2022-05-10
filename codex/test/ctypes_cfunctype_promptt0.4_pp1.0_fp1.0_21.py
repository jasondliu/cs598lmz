import ctypes
# Test ctypes.CFUNCTYPE

import ctypes
from ctypes import wintypes

def func(*args):
    print(args)

LPFUNC = ctypes.CFUNCTYPE(None, *[wintypes.HWND] * 4)

f = LPFUNC(func)
f(0, 0, 0, 0)
# Test ctypes.POINTER

import ctypes
from ctypes import wintypes

def func(*args):
    print(args)

LPFUNC = ctypes.CFUNCTYPE(None, *[ctypes.POINTER(wintypes.HWND)] * 4)

f = LPFUNC(func)
