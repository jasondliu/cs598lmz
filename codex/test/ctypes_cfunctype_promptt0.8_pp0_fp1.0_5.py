import ctypes
# Test ctypes.CFUNCTYPE with a function with struct arguments
#
# This is a test for SF bug #1447804 "ctypesgen fails to compile wrappers for Py_buffer when using CFUNCTYPE"
#
# This bug caused the generated wrappers to be unusable.

from ctypes import *

class Py_buffer(Structure):
    _fields_ = [
        ("buf", c_void_p),
        ("obj", c_void_p),
        ("len", c_int),
        ("itemsize", c_int),

        ("readonly", c_int),
        ("ndim", c_int),
        ("format", c_char_p),
        ("shape", POINTER(c_int)),
        ("strides", POINTER(c_int)),
        ("suboffsets", POINTER(c_int)),
        ("internal", c_void_p),
    ]

F = CFUNCTYPE(c_void_p, POINTER(Py_buffer), c_char_p)

def f(b,s):
    return b,s

