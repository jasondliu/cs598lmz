import ctypes
# Test ctypes.CFUNCTYPE by wrapping a few functions.

import unittest
from test.support import eqtype
from ctypes import *

StructureS = Structure

try:
    from _ctypes import PyObj_FromPtr
except ImportError:
    def PyObj_FromPtr(pointer):
        return pointer

class X(Structure):
    _fields_ = [("a", c_int)]

class Y(Structure):
    _fields_ = [("b", c_char)]

class Z(Structure):
    _fields_ = [("a", c_int), ("b", c_int)]

class F(Structure):
    _fields_ = [("a", c_long)]

class G(Structure):
    _fields_ = [("b", c_char)]

class P(Structure):
    _fields_ = [("p", POINTER(c_char))]


class TestCFuncPtr(unittest.TestCase):

    def test_paramflags(self):
        self.assertEqual(type(CFUNCTYPE(c_
