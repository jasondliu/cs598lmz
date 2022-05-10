import ctypes
# Test ctypes.CField is present and works as expected

import ctypes as ct
import unittest

class Test(unittest.TestCase):
    def test_structure_with_cfield(self):
        class Point(ctypes.Structure):
            _fields_ = [("x", ct.c_uint32),
                        ("y", ct.c_uint32),
                        (ctypes.c_char * 8, "name")]

        p = Point()
        p.x = 123
        p.y = 234
        self.assertEqual(p.x, 123)
        self.assertEqual(p.y, 234)
        p.name = "spam"
        self.assertEqual(p.name, b"spam")

        p2 = Point.from_buffer_copy(p)
        self.assertEqual(p.x, 123)
        self.assertEqual(p.y, 234)
        self.assertEqual(p.name, b"spam")

    def test_structure_with_multiple_cfields(self):
