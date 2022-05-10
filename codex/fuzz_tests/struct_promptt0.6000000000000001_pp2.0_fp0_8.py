import _struct
# Test _struct.Struct
import struct
from test.test_support import bigaddrspacetest
from test import test_support
import unittest
# Issue #7405: _struct.Struct.__repr__() and Struct.format
# should have the same semantics.
class StructTest(unittest.TestCase):

    def test_unnamed(self):
        self.assertRaises(TypeError, _struct.Struct)

    def test_repr(self):
        self.assertEqual(repr(_struct.Struct('h')), "Struct('h')")
        self.assertEqual(repr(_struct.Struct('bb')), "Struct('bb')")
        self.assertEqual(repr(_struct.Struct('hhh')), "Struct('hhh')")
        self.assertEqual(repr(_struct.Struct('hhh')), "Struct('hhh')")
        self.assertEqual(repr(_struct.Struct('i')), "Struct('i')")
        self.assertEqual(repr(_struct.Struct('l')), "Struct('l')")
        self.assertEqual
