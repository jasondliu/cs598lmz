import ctypes
# Test ctypes.CField

# This test is for the CField class.
# It checks that the field is correctly initialized and that the
# __get__, __set__ and __delete__ methods are correctly called.

import unittest
from test import support

from ctypes import *

class X(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int)]

class Y(X):
    _fields_ = [("c", c_int),
                ("d", c_int)]

class Z(Y):
    _fields_ = [("e", c_int),
                ("f", c_int)]

class W(Structure):
    _fields_ = [("g", c_int),
                ("h", c_int)]

class V(Structure):
    _fields_ = [("i", c_int),
                ("j", c_int)]

class U(Structure):
    _fields_ = [("k", c_int),
                ("l", c_int)]

class T(Structure):
    _
