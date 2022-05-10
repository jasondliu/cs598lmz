import _struct
# Test _struct.Struct.

import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        # Test _struct.Struct objects

        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.format, 'i')

        s = _struct.Struct('hhl')
        self.assertEqual(s.size, 8)
        self.assertEqual(s.format, 'hhl')

        # test struct unpacking
