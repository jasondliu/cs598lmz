import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        from ctypes import *
        class X(Structure):
            _fields_ = [("a", c_int),
                        ("b", c_int)]
        p = pointer(X())
        self.assertEqual(p.contents.a, 0)
        self.assertEqual(p.contents.b, 0)

        p.contents.a = 1
        p.contents.b = 2
        self.assertEqual(p.contents.a, 1)
        self.assertEqual(p.contents.b, 2)

        self.assertEqual(p.contents[0], 1)
        self.assertEqual(p.contents[1], 2)

        p.contents[0] = 3
        p.contents[1] = 4
        self.assertEqual(p.contents.a, 3)
        self.assertEqual(p.contents.b, 4)

        self.assertEqual(p
