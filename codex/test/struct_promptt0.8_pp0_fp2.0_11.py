import _struct
# Test _struct.Struct class
import unittest
import struct
import sys
from test import test_support

class StructTestCase(unittest.TestCase):

    def test_basic(self):
        # Test basic packing/unpacking.
        st = _struct.Struct('i')
        data = st.pack(448)
        self.assert_(st.unpack(data) == (448,))

    def test_unpack_from(self):
        # Test basic packing/unpacking.
        st = _struct.Struct('i')
        data = st.pack(448)
        buffer = _array.array('c', data)
        self.assertEqual(st.unpack_from(buffer), (448,))

    def test_pack_into(self):
        # Test basic packing/unpacking.
        st = _struct.Struct('i')
        buffer = _array.array('c', '12345678')
        st.pack_into(buffer, 2, 448)
        self.assertEqual(st.unpack_from(buffer, 2), (448,))

