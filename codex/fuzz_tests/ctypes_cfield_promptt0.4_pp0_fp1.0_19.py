import ctypes
# Test ctypes.CField

if __name__ == '__main__':
    import sys
    import os
    import unittest
    import ctypes

    class X(ctypes.Structure):
        _fields_ = [("a", ctypes.c_int)]
    class Y(ctypes.Structure):
        _fields_ = [("a", ctypes.c_int)]

    class Z(ctypes.Structure):
        _fields_ = [("a", X),
                    ("b", Y)]

    class Test(unittest.TestCase):
        def test_field_name(self):
            self.assertEqual(X.a.name, "a")
            self.assertEqual(Z.a.name, "a")
            self.assertEqual(Z.b.name, "b")

        def test_field_type(self):
            self.assertEqual(X.a.type, ctypes.c_int)
            self.assertEqual(Z.a.type, X)
            self.assertEqual(Z.b.type, Y)


