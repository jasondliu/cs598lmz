import ctypes
# Test ctypes.CField in structures

class X(ctypes.Structure):
    _pack_ = 1
    _fields_ = [("a", ctypes.c_byte),
                ("b", ctypes.CField)]

class Y(ctypes.Structure):
    _pack_ = 1
    _fields_ = [("a", ctypes.c_byte),
                ("b", ctypes.CField("d"))]

class Z(ctypes.Structure):
    _pack_ = 1
    _fields_ = [("a", ctypes.c_byte),
                ("b", ctypes.CField("d", 2))]

if __name__ == "__main__":
    import unittest
    from test import support

    class TestCField(unittest.TestCase):
        def test_x(self):
            x = X()
            self.assertEqual(ctypes.sizeof(x), 2)
            self.assertEqual(x.a, 0)
            self.assertEqual(x.b, 0)

            x = X(3, 4
