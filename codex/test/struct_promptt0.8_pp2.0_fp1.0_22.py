import _struct
# Test _struct.Struct, with format string and format characters.
import unittest
import test.support
from test import support

class StructTestCase(unittest.TestCase):
    def setUp(self):
        self.s = _struct.Struct("i 4s f")

    def test_size(self):
        self.assertEqual(self.s.size, 12)

    def test_pack(self):
        # All optional arguments to pack() must be omitted or None.
        self.assertRaises(TypeError, self.s.pack, 42, "spam", 3.5,
                          1, None)
        self.assertRaises(TypeError, self.s.pack, 42, "spam", 3.5,
                          None, 1)
        self.assertRaises(TypeError, self.s.pack, 42, "spam", 3.5,
                          1)
        self.assertRaises(TypeError, self.s.pack, 42, "spam", 3.5,
                          None)
