import _struct
# Test _struct.Struct.

import os, sys
import unittest

from test import test_support
from test.test_support import bigmemtest

class StructTestCase(unittest.TestCase):

    def test_creation(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, 1, 2, 3)
        self.assertRaises(TypeError, _struct.Struct, 'Zi')
        self.assertRaises(TypeError, _struct.Struct, 'Z#')
        self.assertRaises(TypeError, _struct.Struct, 'Z')
        self.assertRaises(TypeError, _struct.Struct, '1')
        self.assertRaises(TypeError, _struct.Struct, 'Zi', 1)
        self.assertRaises(TypeError, _struct.Struct, 'Z#', 1)
        self.assertRaises(TypeError, _struct.Struct, 'Z', 1)
        self.assertRaises(TypeError, _struct.Struct, '1', 1)
