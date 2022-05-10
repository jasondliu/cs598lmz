import _struct
# Test _struct.Struct.pack_into()

import array
import sys
import unittest

from test import support

class StructTest(unittest.TestCase):

    def test_pack_into(self):
        # Issue #16093: pack_into() should return None
        s = _struct.Struct('i')
        a = array.array('i', [0])
        self.assertIsNone(s.pack_into(a, 0, 42))
        self.assertEqual(a[0], 42)

    def test_pack_into_buffer(self):
        # Issue #16093: pack_into() should return None
        s = _struct.Struct('i')
        a = array.array('i', [0])
        self.assertIsNone(s.pack_into(a, 0, 42))
        self.assertEqual(a[0], 42)

    def test_pack_into_offset(self):
        # Issue #16093: pack_into() should return None
        s = _struct.Struct('i')
