import _struct
# Test _struct.Struct

import unittest

class StructTest(unittest.TestCase):

    def test_struct(self):
        self.assertEqual(_struct.Struct('i').size, 4)
        self.assertEqual(_struct.Struct('i').pack(42), b'*\x00\x00\x00')
        self.assertEqual(_struct.Struct('i').unpack(b'*\x00\x00\x00'), (42,))
        self.assertEqual(_struct.Struct('i').unpack_from(b'\x00\x00\x00*'), (42,))
        self.assertEqual(_struct.Struct('i').unpack_from(memoryview(b'\x00\x00\x00*')), (42,))
        self.assertEqual(_struct.Struct('i').unpack_from(bytearray(b'\x00\x00\x00*')), (42,))
