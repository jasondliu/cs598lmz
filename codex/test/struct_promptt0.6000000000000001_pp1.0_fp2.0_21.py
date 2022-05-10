import _struct
# Test _struct.Struct
import struct
import sys
import unittest
import test.support

class StructTestCase(unittest.TestCase):
    def test_creation(self):
        # Create struct objects
        st = _struct.Struct('i')
        self.assertEqual(st.size, 4)
        self.assertEqual(st.format, 'i')
        st = _struct.Struct('cb?')
        self.assertEqual(st.size, 4)
        self.assertEqual(st.format, 'cb?')
        st = _struct.Struct('iii')
        self.assertEqual(st.size, 12)
        self.assertEqual(st.format, 'iii')
        st = _struct.Struct('hhhh')
        self.assertEqual(st.size, 8)
        self.assertEqual(st.format, 'hhhh')
        st = _struct.Struct('hhiq')
        self.assertEqual(st.size, 16)
        self.assertEqual(st.format, 'hhiq')
        st = _
