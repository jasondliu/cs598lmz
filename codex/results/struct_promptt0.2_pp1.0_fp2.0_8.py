import _struct
# Test _struct.Struct

import unittest
import sys

class StructTest(unittest.TestCase):

    def test_struct(self):
        # Test _struct.Struct
        import _struct
        self.assertEqual(_struct.Struct('h').size, 2)
        self.assertEqual(_struct.Struct('i').size, 4)
        self.assertEqual(_struct.Struct('l').size, 4)
        self.assertEqual(_struct.Struct('q').size, 8)
        self.assertEqual(_struct.Struct('H').size, 2)
        self.assertEqual(_struct.Struct('I').size, 4)
        self.assertEqual(_struct.Struct('L').size, 4)
        self.assertEqual(_struct.Struct('Q').size, 8)
        self.assertEqual(_struct.Struct('f').size, 4)
        self.assertEqual(_struct.Struct('d').size, 8)
        self.assertEqual(_struct.Struct('P').size, _struct.calcsize('P'))
        self.assertE
