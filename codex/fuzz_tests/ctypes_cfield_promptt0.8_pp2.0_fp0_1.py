import ctypes
# Test ctypes.CField

import ctypes
import unittest

class TestCField(unittest.TestCase):
    def test_create_instance(self):
        class x(ctypes.Structure):
            _fields_ = [("a", ctypes.c_long),
                        ("b", ctypes.c_long)]

        class y(ctypes.Structure):
            _fields_ = [("x", x),
                        ("c", ctypes.c_long)]

        obj = y(x(1, 2), 3)
        self.assertEqual(obj.x.a, 1)
        self.assertEqual(obj.x.b, 2)
        self.assertEqual(obj.c, 3)

        self.assertEqual(obj.x[0], 1)
        self.assertEqual(obj.x[1], 2)
        self.assertEqual(obj.c[0], 3)

        self.assertEqual(obj[0].a, 1)
        self.assertEqual(obj[0].b, 2)
        self.assertE
