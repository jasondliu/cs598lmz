import _struct
# Test _struct.Struct()

import unittest

from test import support

class StructTestCase(unittest.TestCase):

    def test_basic(self):
        s = _struct.Struct('hhl')
        self.assertEqual(s.size, 8)
        self.assertEqual(s.pack(1, 2, 3), (b'\x01\x00\x02\x00\x00\x00\x00\x03'))
        self.assertEqual(s.unpack(b'\x01\x00\x02\x00\x00\x00\x00\x03'), (1, 2, 3))
        self.assertEqual(s.unpack_from(b'\x01\x00\x02\x00\x00\x00\x00\x03\x04\x05'), (1, 2, 3))
        self.assertEqual(s.unpack_from(b'*' * 100, 2), (256, 512, 131072))

    def test_unicode_format(self):
