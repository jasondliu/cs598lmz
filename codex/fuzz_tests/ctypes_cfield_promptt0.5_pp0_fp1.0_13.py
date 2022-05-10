import ctypes
# Test ctypes.CField

import sys
import ctypes
from ctypes import *

class X(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int)]

class Y(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int),
                ("c", c_int),
                ("d", c_int)]

class Z(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int),
                ("c", c_int),
                ("d", c_int)]

class BigStruct(Structure):
    _fields_ = [("x", X),
                ("y", Y),
                ("z", Z),
                ("w", c_int)]

# Alignment and packing

class A(Structure):
    _fields_ = [("a", c_byte),
                ("b", c_int)]

class B(Structure):
    _pack_ = 2
    _fields_ = [("a", c_byte),
               
