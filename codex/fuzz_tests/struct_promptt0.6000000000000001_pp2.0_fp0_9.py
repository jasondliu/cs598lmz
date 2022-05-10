import _struct
# Test _struct.Struct objects

from test import support
import unittest

from array import array

from _testcapi import getargs_b, getargs_B, getargs_h, getargs_H, getargs_i, \
    getargs_I, getargs_l, getargs_L, getargs_q, getargs_Q, getargs_f, \
    getargs_d, getargs_P, getargs_s, getargs_y, getargs_u

import sys

class StructTestCase(unittest.TestCase):

    def test_struct_error(self):
        self.assertRaises(ValueError, _struct.Struct, 'abcdef')
        self.assertRaises(ValueError, _struct.Struct, 'abcdef', 0)
        self.assertRaises(ValueError, _struct.Struct, 'abcdef', 0, 0)
        self.assertRaises(ValueError, _struct.Struct, 'abcdef', 0, 0, 0)

        self.assertRaises(TypeError, _struct.Struct, None)
        self.assertRa
