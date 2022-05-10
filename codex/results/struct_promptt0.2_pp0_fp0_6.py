import _struct
# Test _struct.Struct.

import sys
import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct_doc(self):
        # Test that the docstring is useful.
        self.assertTrue(len(_struct.Struct.__doc__) > 100)

    def test_struct_unpack(self):
        # Test struct.unpack().
        s = _struct.Struct('i')
        self.assertEqual(s.unpack(b'abcd'), (1633837924,))
        self.assertEqual(s.unpack(b'abcd', 2), (1633837924,))
        self.assertRaises(struct.error, s.unpack, b'abc')
        self.assertRaises(struct.error, s.unpack, b'abc', 2)
        self.assertRaises(struct.error, s.unpack, b'abc', 1)
        self.assertRaises(struct.error, s.unpack, b'abc', 3)
        self.assertRaises(struct.error
