import ctypes
# Test ctypes.CField
from ctypes import *
from ctypes.test import need_symbol
import sys

libc = CDLL(ctypes.util.find_library("c"))

class X(Structure):
    pass

X._fields_ = [("x", c_int)]

class POINTER(object):
    def __init__(self, ptr):
        self.ptr = ptr

class Y(Structure):
    _fields_ = [("p", POINTER(X))]

y = Y()

class Z(Structure):
    _fields_ = [("p", POINTER(POINTER(X)))]

z = Z()

class S(Structure):
    _fields_ = [("p", POINTER(c_char_p))]

s = S()

class T(Structure):
    _fields_ = [("p", c_void_p)]

t = T()

class U(Structure):
    _fields_ = [("p", POINTER(c_void_p))]

u = U()

class V
