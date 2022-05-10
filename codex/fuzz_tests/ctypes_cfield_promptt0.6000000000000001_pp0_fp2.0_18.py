import ctypes
# Test ctypes.CField
#

if __name__ == "__main__":
    import test.test_support
    import unittest

    class CFieldTestCase(unittest.TestCase):

        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
            class Y(ctypes.Union):
                _fields_ = [("c", ctypes.c_int),
                            ("d", ctypes.c_float)]

        def test_fields(self):
            self.assertEqual(self.X._fields_, [("a", ctypes.c_int),
                                               ("b", ctypes.c_int)])
            self.assertEqual(self.X.Y._fields_, [("c", ctypes.c_int),
                                                 ("d", ctypes.c_float)])

        def test_getattr(self):
            x = self.X()
            self.assertEqual(x.a, 0)
            self.assertEqual(
