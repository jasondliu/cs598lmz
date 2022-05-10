import _struct
# Test _struct.Struct objects.
from test import test_support
import unittest
from array import array

class StructTest(unittest.TestCase):
    def test_unpack_from(self):
        # Test _struct.unpack_from()
        # Format 'xi'
        x = array('b', [1, 0, 0, 0, 2, 0, 0, 0])
        s = _struct.Struct('xi')
        self.assertEqual(s.unpack_from(x, 0), (1, 2))
        self.assertEqual(s.unpack_from(x, 1), (1, 2))
        self.assertEqual(s.unpack_from(x, 2), (16777216, 2))
        self.assertEqual(s.unpack_from(x, 3), (16777216, 2))
        self.assertEqual(s.unpack_from(x, 4), (2, 2))
        self.assertEqual(s.unpack_from(x, 5), (2, 2))
        self.assertEqual
