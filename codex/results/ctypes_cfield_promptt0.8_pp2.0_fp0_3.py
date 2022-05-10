import ctypes
# Test ctypes.CField.from_param
#
# Written by Thomas Heller, 2002
#

import unittest
from ctypes import *

class X(Structure):
    _fields_ = [("a", c_int),
                ("b", c_char),
                ("c", c_char * 2),
                ("d", c_char * 2)]

    def f(self):
        pass

class Y(X):
    _fields_ = X._fields_ + [("e", c_long)]

class Simple(Structure):
    _fields_ = [("a", c_int), ("b", c_int),
                ("c", c_char), ("d", c_char),
                ("e", c_char * 2)]

class Z(Simple):
    _fields_ = Simple._fields_ + [("f", c_int),
                                  ("g", c_int)]

class AddressOfTestCase(unittest.TestCase):
    def test_address_of(self):
        self.assertEqual(addressof(X.a), ctypes.addresso
