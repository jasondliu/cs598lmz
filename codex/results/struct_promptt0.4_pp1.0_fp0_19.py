import _struct
# Test _struct.Struct
#
# This test checks the basic functionality of the _struct module.

import _struct
import unittest
from test import support

class StructTest(unittest.TestCase):
    def test_format(self):
        self.assertRaises(ValueError, _struct.Struct, "")
        self.assertRaises(ValueError, _struct.Struct, "A")
        self.assertRaises(ValueError, _struct.Struct, "1")
        self.assertRaises(ValueError, _struct.Struct, "11")
        self.assertRaises(ValueError, _struct.Struct, "Bhil")
        self.assertRaises(ValueError, _struct.Struct, "BhilB")
        self.assertRaises(ValueError, _struct.Struct, "BhilBB")
        self.assertRaises(ValueError, _struct.Struct, "BhilBBB")
        self.assertRaises(ValueError, _struct.Struct, "BhilBBBB")
        self.assertRaises(ValueError, _struct.Struct, "
