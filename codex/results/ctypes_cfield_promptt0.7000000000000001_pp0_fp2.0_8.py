import ctypes
# Test ctypes.CField
from ctypes import *
import _ctypes_test
from _ctypes_test import get_type

from test.support import import_module
ctypes_test = import_module('_ctypes_test')

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    def __init__(self):
        self.a = 1
        self.b = 1

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", X)]
    def __init__(self):
        self.x = X()
        self.y = X()

class Z(ctypes.Structure):
    _fields_ = [("y", Y),
                ("z", Y)]
    def __init__(self):
        self.y = Y()
        self.z = Y()

class ArrayTestCase(unittest.TestCase):
    def test_array(self):
        class X(ctypes.Structure
