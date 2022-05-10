import _struct
# Test _struct.Struct class

class TestStruct(unittest.TestCase):

    def test_unpack(self):
        # Issue #5731: struct.unpack should return a tuple, even for fmt='x'
        self.assertEqual(_struct.unpack('x', b'x'), (None,))
        self.assertEqual(_struct.unpack('x', b'x\x00'), (None, b'\x00'))
        self.assertEqual(_struct.unpack('xc', b'x\x00'), (None, b'\x00'))
        self.assertEqual(_struct.unpack('xcb', b'x\x00\x01'), (None, b'\x00\x01'))

    def test_pack_into(self):
        # Issue #5731: struct.pack_into should accept a bytearray
        ba = bytearray(b'xxxxxx')
        _struct.pack_into('x', ba, 3)
        self.assertEqual(ba, bytearray(b'xxx\x00\x
