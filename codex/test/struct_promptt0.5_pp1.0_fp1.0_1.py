import _struct
# Test _struct.Struct and _struct.calcsize()

import _struct
import test.test_support
import unittest

class StructTest(unittest.TestCase):

    def test_struct(self):
        st = _struct.Struct('i')
        self.assertEqual(st.size, 4)
        self.assertEqual(st.pack(12345), '\x39\x30\x00\x00')
        self.assertEqual(st.unpack('\x39\x30\x00\x00'), (12345,))
        self.assertEqual(st.unpack_from('zz\x39\x30\x00\x00zz', 2), (12345,))
        self.assertEqual(st.pack_into('zz\x39\x30\x00\x00zz', 2, 67890), None)
        self.assertEqual(st.unpack('zz\x39\x30\x00\x00zz', 2), (12345,))

        st = _struct.Struct('i')
