import ctypes
# Test ctypes.CFUNCTYPE and a subclass of ctypes.Structure.
# It checks that the callee receives the correct type of argument.
# Test needs -fPIC on linux.

from ctypes import *
from ctypes.test import is_resource_enabled
import unittest
from test import support

# ctypes.c_long is used because on i386 Windows it's an alias for c_int
class POINT(Structure):
    _fields_ = [('x', c_long), ('y', c_long)]

class POINTP(Structure):
    _fields_ = [('point', POINT), ('tag', c_long)]

class TestSubclassStructure(unittest.TestCase):

    def wrap(self, name):
        func = getattr(self.lib, name)
        func.restype = POINT
        func.argtypes = [POINTP]
        return func

    def setUp(self):

        if is_resource_enabled('printing'):
            set_conversion_mode("all", "error")

        if hasattr(self, '
