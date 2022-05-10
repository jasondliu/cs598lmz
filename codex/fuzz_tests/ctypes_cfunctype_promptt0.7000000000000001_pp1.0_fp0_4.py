import ctypes
# Test ctypes.CFUNCTYPE()

from ctypes import *
from ctypes import wintypes

import unittest

# for dumping the function prototype
import sys

from sys import platform
if platform == "darwin":
    from ctypes import objc

# for sizeof
import struct

# for isinstance(x, integer_types)
from ctypes import _simple_type_cache
integer_types = _simple_type_cache[int]

import _ctypes_test

def get_wintype(name):
    return getattr(wintypes, name)

# wintypes.BOOL is only defined on windows
if hasattr(wintypes, 'BOOL'):
    BOOL = wintypes.BOOL
else:
    BOOL = c_int

class Structures(unittest.TestCase):
    def test_structure_1(self):
        class X1(Structure):
            _fields_ = [("x", c_int)]

        x = X1()
        x.x = 42
        self.assertEqual(x.x
