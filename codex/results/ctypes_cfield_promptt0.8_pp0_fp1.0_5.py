import ctypes
# Test ctypes.CField and ctypes.CStruct.from_address
from ctypes import *

class TestFromAddress(unittest.TestCase):

    def test_from_address(self):
        class POINT(Structure):
            _fields_ = [("x", c_long),
                        ("y", c_long)]

        pt = POINT()
        pt.x = 123
        pt.y = 234
        a = addressof(pt)

        pt2 = POINT.from_address(a)
        self.assertEqual(pt2.x, 123)
        self.assertEqual(pt2.y, 234)

        try:
            POINT.from_address(-1)
        except OSError:
            pass
        else:
            self.fail("from_address(-1) should fail")

    def test_from_address_incomplete_structure(self):
        class X(Structure):
            _fields_ = [("a", c_int)]
        x = X.from_address(0)

    def test_from_address_incomplete_
