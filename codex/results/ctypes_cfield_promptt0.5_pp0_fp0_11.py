import ctypes
# Test ctypes.CField
#
# A CField is a CFieldDescriptor that uses a ctypes type instead of a
# struct format string.

import unittest
from test.support import run_unittest

from ctypes import *

class X(Structure):
    _fields_ = [("a", c_char),
                ("b", c_int),
                ("c", c_double)]
    _anonymous_ = ["a"]

class Y(Structure):
    _fields_ = [("a", c_char),
                ("b", c_int),
                ("c", c_double)]
    _anonymous_ = [("a", c_char), ("b", c_int)]

class Z(Structure):
    _fields_ = [("a", c_char),
                ("b", c_int),
                ("c", c_double)]
    _anonymous_ = [("a", c_char), ("b", c_int), ("c", c_double)]

class Test(unittest.TestCase):
    def test_one(self):

