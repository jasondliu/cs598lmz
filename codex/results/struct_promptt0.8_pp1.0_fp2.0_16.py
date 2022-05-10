import _struct
# Test _struct.Struct
#
# Instantiate a new Struct object for each format.
#
# This is a cleaned up version of test_struct.py taken from the
# Python regression tests.

import struct
import unittest
from test import support

import sys as _sys


class StructTestCase(unittest.TestCase):
    def test_new_error(self):
        self.assertRaises(TypeError, _struct.Struct, 'c')
        self.assertRaises(TypeError, _struct.Struct, 'd', 'abc')
        self.assertRaises(TypeError, _struct.Struct, 'I', 42)

    def test_format(self):
        st = _struct.Struct('hhl')
        self.assertEqual(st.format, 'hhl')

        with self.assertRaises(TypeError):
            st.format = 'c'
        with self.assertRaises(TypeError):
            st.format = 42
        with self.assertRaises(TypeError):
            st.format = 'cc'

        # create a new struct object by format

