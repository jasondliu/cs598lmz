import ctypes
# Test ctypes.CFUNCTYPE()

from ctypes import *
from ctypes.test import need_symbol

def func(*args):
    print(args)

#CFUNCTYPE(None, c_int, c_int)(func)(1, 2)

#CFUNCTYPE(c_int, c_int, c_int)(func)(1, 2)

#CFUNCTYPE(c_int, c_int, c_int)(func)

#CFUNCTYPE(c_int, c_int, c_int)

#CFUNCTYPE(c_int, c_int)

#CFUNCTYPE(c_int)

#CFUNCTYPE(c_int, c_int, c_int, c_int)

#CFUNCTYPE(c_int, c_int, c_int, c_int, c_int)

#CFUNCTYPE(c_int, c_int, c_int, c_int, c_int, c_int)

#CFUNCTYPE(c
