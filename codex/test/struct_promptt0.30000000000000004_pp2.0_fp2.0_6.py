import _struct
# Test _struct.Struct

import sys
import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct_bytesize(self):
        self.assertEqual(_struct.Struct('i').size, 4)
        self.assertEqual(_struct.Struct('ii').size, 8)
        self.assertEqual(_struct.Struct('iii').size, 12)
        self.assertEqual(_struct.Struct('iiii').size, 16)
        self.assertEqual(_struct.Struct('iiiii').size, 20)
        self.assertEqual(_struct.Struct('iiiiii').size, 24)
        self.assertEqual(_struct.Struct('iiiiiii').size, 28)
        self.assertEqual(_struct.Struct('iiiiiiii').size, 32)
        self.assertEqual(_struct.Struct('iiiiiiiii').size, 36)
        self.assertEqual(_struct.Struct('iiiiiiiiii').size, 40)
