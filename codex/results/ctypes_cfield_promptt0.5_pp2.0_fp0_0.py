import ctypes
# Test ctypes.CField
import _ctypes_test

class CTest(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.c_int),
        ('c', ctypes.c_int),
        ('d', ctypes.c_int),
        ('e', ctypes.c_int),
        ('f', ctypes.c_int),
        ('g', ctypes.c_int),
    ]

class Test(unittest.TestCase):
    def test_field(self):
        # Test the ctypes.CField attribute
        c = CTest()
        self.assertEqual(c.a, 0)
        self.assertEqual(c.b, 0)
        self.assertEqual(c.c, 0)
        self.assertEqual(c.d, 0)
        self.assertEqual(c.e, 0)
        self.assertEqual(c.f, 0)
        self.assertEqual(c.g, 0)

        c.a =
