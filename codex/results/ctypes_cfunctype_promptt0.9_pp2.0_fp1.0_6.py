import ctypes
# Test ctypes.CFUNCTYPE()

import sys
if sys.platform == "win32":
    from _ctypes import COMError
else:
    COMError = None

from ctypes import *
import _ctypes_test

lib = cdll.msvcrt

@CFUNCTYPE(c_int, c_int)
def func_int(arg):
    print("called func_int() with", arg)
    return arg * 5

@CFUNCTYPE(c_char_p)
def func_char_p():
    s = b"hello world"
    print("called func_char_p()")
    return s

@CFUNCTYPE(c_int, POINTER(c_int))
def func_ptr(arg):
    print("called func_ptr() with", arg[0])
    return arg[0] * 5

@CFUNCTYPE(c_double, c_double)
def func_double(arg):
    print("called func_double() with", arg)
    return arg * 5

@CFUNCTYPE(
