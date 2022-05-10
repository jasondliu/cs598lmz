import _struct
# Test _struct.Struct module.

import unittest
import struct
import sys

class StructTestCase(unittest.TestCase):

    def test_struct_error(self):
        # SF bug #525858
        self.assertRaises(TypeError, struct.Struct, 'abc', 42)
        self.assertRaises(TypeError, struct.Struct, 'abc', 0, 42)
        self.assertRaises(struct.error, struct.Struct, 'q')
        self.assertRaises(struct.error, struct.Struct, 'P')
        self.assertRaises(struct.error, struct.Struct, 'x')
        self.assertRaises(struct.error, struct.Struct, 'cx')
        self.assertRaises(struct.error, struct.Struct, 'Px')
        self.assertRaises(struct.error, struct.Struct, 'cP')
        self.assertRaises(struct.error, struct.Struct, 'cP', 0)
        self.assertRaises(struct.error, struct.Struct, 'bxx')
        self.assertRaises
