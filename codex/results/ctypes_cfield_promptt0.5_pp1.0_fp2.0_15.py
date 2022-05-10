import ctypes
# Test ctypes.CField
import ctypes._testcapi as _testcapi

from ctypes import *
from ctypes.test import need_symbol

class X(Structure):
    _fields_ = [("a", c_char),
                ("b", c_char),
                ("c", c_char),
                ("d", c_char)]

class Y(Structure):
    _fields_ = [("a", c_char),
                ("b", c_char),
                ("c", c_char),
                ("d", c_char)]

class Z(Structure):
    _fields_ = [("a", c_char),
                ("b", c_char),
                ("c", c_char),
                ("d", c_char)]

class Test(unittest.TestCase):
    def test_fields(self):
        self.assertEqual(X._fields_, [("a", c_char),
                                      ("b", c_char),
                                      ("c", c_char),
                                      ("d", c_char)])
        self.assert
