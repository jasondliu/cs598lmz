import _struct
# Test _struct.Struct
#
# The test cases are taken from the Python 2.7.2 documentation for the
# struct module.

import unittest
from test import test_support

class StructTestCase(unittest.TestCase):

    def test_unpack(self):
        st = _struct.Struct('i')
        self.assertEqual(st.unpack('\x01\x00\x00\x00'), (1,))
        self.assertEqual(st.unpack('\x01\x00\x00\x00Junk'), (1,))
        self.assertRaises(TypeError, st.unpack, 'foo')
        self.assertRaises(TypeError, st.unpack, 'foo', 1)
        self.assertRaises(TypeError, st.unpack, 'foo', 1, 2)
        self.assertRaises(TypeError, st.unpack, 'foo', 1, 2, 3)
        self.assertRaises(TypeError, st.unpack, 'foo', 1, 2, 3, 4)
        self.assertRa
