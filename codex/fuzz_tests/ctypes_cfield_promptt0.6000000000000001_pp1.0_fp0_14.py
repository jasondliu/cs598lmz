import ctypes
# Test ctypes.CField.from_address

import unittest

from ctypes import *

class CFoo(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int)]

class CFoo2(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int),
                ("c", c_int)]

class TestFromAddress(unittest.TestCase):
    def test_fromaddress(self):
        p = pointer(CFoo(1, 2))
        f = CFoo.from_address(addressof(p.contents))
        self.assertEqual(f.a, 1)
        self.assertEqual(f.b, 2)

    def test_fromaddress_bad(self):
        f = CFoo.from_address(addressof(CFoo2(0,0,0)))
        self.assertEqual(f.a, 0)
        self.assertEqual(f.b, 0)


if __name__ == '__main__':
    un
