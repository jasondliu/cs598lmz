import _struct
# Test _struct.Struct().
class TestStruct(unittest.TestCase):
    def test_struct(self):
        self.assertEqual(struct.calcsize('hhi'), _struct.calcsize('hhi'))
        self.assertEqual(struct.pack('hhi', 1, 2, 3),
                         _struct.pack('hhi', 1, 2, 3))
        self.assertEqual(struct.unpack('hhi', b'\x01\x00\x02\x00\x00\x00\x03\x00\x00\x00'),
                         _struct.unpack('hhi', b'\x01\x00\x02\x00\x00\x00\x03\x00\x00\x00'))
        self.assertEqual(struct.pack('hh', 1, 2),
                         _struct.pack('hh', 1, 2))
        self.assertEqual(struct.unpack('hh', b'\x01\x00\x02\x00'),
                         _struct.unpack('hh', b'\x
