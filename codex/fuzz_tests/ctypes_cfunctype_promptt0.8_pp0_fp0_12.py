import ctypes
# Test ctypes.CFUNCTYPE.

from ctypes import *
import unittest

try:
    c_uint128
except NameError:
    c_uint128 = c_uint64

CALLBACK_FUNCTYPE = WINFUNCTYPE(c_uint, c_int, c_int, c_int, c_int, c_int)

class TestCFuncPtr(unittest.TestCase):

    def test_instance_int(self):
        target = c_int.from_address(0x12345678)
        callback = CALLBACK_FUNCTYPE(target)
        self.failUnlessEqual(target._objects, {callback: True})

    def test_instance_instance(self):
        target = c_float(2.0)
        callback = CALLBACK_FUNCTYPE(target)
        self.failUnlessEqual(target._objects, {callback: True})

    def test_instance_instance_raw(self):
        target = c_float(2.0)
        cb = CALLBACK_FUNCTYPE(target.value)
       
