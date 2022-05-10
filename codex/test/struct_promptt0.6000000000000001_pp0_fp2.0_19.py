import _struct
# Test _struct.Struct

import sys
import unittest
from test import support


class StructTestCase(unittest.TestCase):

    def test_struct_docstring(self):
        # Test that the __doc__ attribute for _struct.Struct is set
        # correctly.
        self.assertIn('format', _struct.Struct.__doc__)

    def test_unpack_from(self):
        # Test the optional buffer argument to unpack_from().
        s = _struct.Struct('hhl')
        self.assertEqual(s.unpack_from(b'\0\1\0\0\2\0\0\3'), (1, 2, 3))
        self.assertEqual(s.unpack_from(b'\0\1\0\0\2\0\0\3', 4), (2, 3))
        self.assertEqual(s.unpack_from(b'\0\1\0\0\2\0\0\3', 2), (512, 768))
