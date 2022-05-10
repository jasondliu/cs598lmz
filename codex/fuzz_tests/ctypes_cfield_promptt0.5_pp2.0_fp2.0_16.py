import ctypes
# Test ctypes.CField instance

import unittest
from ctypes import *

class X(Structure):
    _fields_ = [("x", c_int)]

class Y(Structure):
    _fields_ = [("y", c_int)]

class Z(Structure):
    _fields_ = [("z", X)]

class A(Structure):
    _fields_ = [("a", POINTER(c_int))]

class B(Structure):
    _fields_ = [("b", POINTER(POINTER(c_int)))]

class C(Structure):
    _fields_ = [("c", POINTER(POINTER(POINTER(c_int))))]

class D(Structure):
    _fields_ = [("d", POINTER(POINTER(POINTER(POINTER(c_int)))))
                ]

class E(Structure):
    _fields_ = [("e", POINTER(POINTER(POINTER(POINTER(POINTER(c_int))))))
                ]

class F(Structure):
    _fields_
