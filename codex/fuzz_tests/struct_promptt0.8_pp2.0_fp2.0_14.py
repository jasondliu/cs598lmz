import _struct
# Test _struct.Struct with alignment requirements

import _struct as struct
import unittest

class StructTest(unittest.TestCase):
    def test_format(self):
        # The format string is the first argument to the struct constructor.
        # http://docs.python.org/library/struct.html#format-characters
        self.assertRaises(TypeError, struct.Struct, 12)
        self.assertRaises(TypeError, struct.Struct, 12.34)
        self.assertRaises(TypeError, struct.Struct, "12")
        self.assertRaises(TypeError, struct.Struct, "12.34")
        self.assertRaises(TypeError, struct.Struct, "A12.34")
        self.assertRaises(TypeError, struct.Struct, [])
        self.assertRaises(TypeError, struct.Struct, {})
        self.assertRaises(TypeError, struct.Struct, ())
        self.assertRaises(TypeError, struct.Struct, "")
        self.assertRaises(TypeError, struct.Struct, ">")
        self
