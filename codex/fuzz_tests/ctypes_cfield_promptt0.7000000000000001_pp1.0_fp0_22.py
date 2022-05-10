import ctypes
# Test ctypes.CField.from_address

from ctypes import *
from ctypes.test import need_symbol
import unittest

from ctypes.test.test_cfield import FieldTestCase
from ctypes.test.test_cfuncs import ParseError, testfunc
from ctypes.test.test_cfuncs import _testfunc as testfunc_nosegfault


class FromAddressTestCase(FieldTestCase):

    def test_from_address_byval(self):
        class X(Structure):
            _fields_ = [("x", c_int)]
        self.assertRaises(NotImplementedError, CField.from_address,
                          byref(X()), byref(X().x))

    def test_from_address_byref(self):
        class X(Structure):
            _fields_ = [("x", c_int)]
        p = pointer(X())
        self.assertRaises(NotImplementedError, CField.from_address,
                          p, byref(X().x))

    def test_from_
