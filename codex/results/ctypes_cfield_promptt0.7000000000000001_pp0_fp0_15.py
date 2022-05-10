import ctypes
# Test ctypes.CField.from_address

import unittest
from test.support import import_module
from test.support import cpython_only, run_unittest
ctypes = import_module('ctypes')

class StructTest(unittest.TestCase):
    @cpython_only
    def test_from_address(self):
        if ctypes.sizeof(ctypes.c_short) != 2:
            self.skipTest("sizeof(c_short) != 2")
        class S(ctypes.Structure):
            _fields_ = [("foo", ctypes.c_short)]

        s = S()

        field = ctypes.CField.from_address(ctypes.addressof(s), ctypes.c_short)
        self.assertIs(field._type_, ctypes.c_short)
        self.assertEqual(field.offset, 0)
        self.assertEqual(field.size, 2)
        self.assertEqual(field.name, None)

        field = ctypes.CField.from_address(ctypes.add
