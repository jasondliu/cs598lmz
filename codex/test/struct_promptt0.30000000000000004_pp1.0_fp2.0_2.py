import _struct
# Test _struct.Struct

import unittest
import sys
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct_format(self):
        # Issue #7995: struct.Struct.format should be a read-only property
        with self.assertRaises(AttributeError):
            struct.Struct('i').format = 'i'

    def test_struct_size(self):
        # Issue #7995: struct.Struct.size should be a read-only property
        with self.assertRaises(AttributeError):
            struct.Struct('i').size = 4

    def test_struct_unpack_from(self):
        # Issue #7995: struct.Struct.unpack_from should be a read-only property
        with self.assertRaises(AttributeError):
            struct.Struct('i').unpack_from = struct.Struct('i').unpack_from

