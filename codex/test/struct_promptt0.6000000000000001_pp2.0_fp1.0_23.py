import _struct
# Test _struct.Struct
from _struct import *

# Tests for _struct.Struct
import unittest
from unittest import TestCase

class StructTest(TestCase):

    def test_constructor(self):
        self.assertRaises(TypeError, Struct)
        self.assertRaises(TypeError, Struct, 1)
        self.assertRaises(TypeError, Struct, '', 1)
        self.assertRaises(TypeError, Struct, '', '', 1)
        self.assertRaises(TypeError, Struct, '', (), 1)
        self.assertRaises(TypeError, Struct, '', (), None)
        self.assertRaises(TypeError, Struct, '', (), 'c')

    def test_unpack_from(self):
        self.assertRaises(TypeError, Struct('c').unpack_from, None)
        self.assertRaises(TypeError, Struct('c').unpack_from, 1)
        self.assertRaises(TypeError, Struct('c').unpack_from, 'c')
