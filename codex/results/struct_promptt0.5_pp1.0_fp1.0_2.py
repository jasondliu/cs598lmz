import _struct
# Test _struct.Struct
class TestStruct(unittest.TestCase):
    def test_struct(self):
        # Test pack/unpack
        self.assertEqual(_struct.pack('=HI', 1, 2), b'\x00\x01\x00\x02')
        self.assertEqual(_struct.unpack('=HI', b'\x00\x01\x00\x02'), (1, 2))

        # Test pack_into/unpack_from
        buf = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00')
        _struct.pack_into('=HI', buf, 0, 1, 2)
        self.assertEqual(buf, b'\x00\x01\x00\x02\x00\x00\x00\x00')
        self.assertEqual(_struct.unpack_from('=HI', buf, 0), (1, 2))

        # Test iter_unpack
        self.assertEqual(list(_struct.iter_unpack('
