import ctypes
# Test ctypes.CField
#
# <http://docs.python.org/release/2.5.2/lib/ctypes-field-objects.html>

import unittest
from test import test_support

try:
    ctypes
except NameError:
    raise unittest.SkipTest, "ctypes not available"

class CFieldTestCase(unittest.TestCase):
    def test_fields(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int),
                        ("c", ctypes.c_int),
                        ("d", ctypes.c_int),
                        ("e", ctypes.c_int),
                        ("f", ctypes.c_int),
                        ("g", ctypes.c_int),
                        ("h", ctypes.c_int),
                        ("i", ctypes.c_int),
                        ("j", ctypes.c_int),
                        ("k", ctypes.c_int),
                        ("l", ctypes.c_
