import ctypes
# Test ctypes.CField.from_address()

import unittest
from test import test_support

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class CFieldTestCase(unittest.TestCase):
    def test_from_address(self):
        x = X()
        addr = ctypes.addressof(x)
        self.assertEqual(ctypes.c_int.from_address(addr).value, 0)
        x.a = 42
        self.assertEqual(ctypes.c_int.from_address(addr).value, 42)

def test_main():
    test_support.run_unittest(CFieldTestCase)

if __name__ == "__main__":
    test_main()
