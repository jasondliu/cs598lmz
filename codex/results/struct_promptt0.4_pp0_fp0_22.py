import _struct
# Test _struct.Struct

import unittest
from test import test_support
import sys

class StructTestCase(unittest.TestCase):

    def test_struct_error(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, '', 0)
        self.assertRaises(TypeError, _struct.Struct, '', ())
        self.assertRaises(TypeError, _struct.Struct, '', (0,))
        self.assertRaises(TypeError, _struct.Struct, '', (0, 0))
        self.assertRaises(TypeError, _struct.Struct, '', (0, 0, 0))
        self.assertRaises(TypeError, _struct.Struct, '', (0, 0, 0, 0))
        self.assertRaises(TypeError, _struct.Struct, '', (0, 0, 0, 0, 0))
        self.assertRaises(TypeError, _struct.Struct, '', (0, 0, 0, 0, 0, 0))
        self
