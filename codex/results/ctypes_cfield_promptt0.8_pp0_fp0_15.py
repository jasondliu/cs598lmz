import ctypes
# Test ctypes.CField() object
import sys
if sys.version_info >= (2, 7):
    import unittest

    class CFoo(ctypes.Structure):
        _fields_ = [("a", ctypes.c_int),
                    ("b", ctypes.c_int),
                    (ctypes.CField("c", ctypes.c_int)),
                    (ctypes.CField("d", ctypes.c_int))]

    class Test(unittest.TestCase):
        def test_CField(self):
            self.assertEqual(CFoo.a.offset, 0)
            self.assertEqual(CFoo.b.offset, 4)
            self.assertEqual(CFoo.c.offset, 8)
            self.assertEqual(CFoo.d.offset, 12)

            self.assertEqual(CFoo.a.size, 4)
            self.assertEqual(CFoo.c.size, 4)

    if __name__ == "__main__":
        unittest.main()
