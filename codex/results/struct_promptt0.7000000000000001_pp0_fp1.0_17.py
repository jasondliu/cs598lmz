import _struct
# Test _struct.Struct

class TestStruct(unittest.TestCase):
    def test_struct(self):
        s = _struct.Struct('hhi')
        self.assertEqual(s.size, struct.calcsize('hhi'))
        self.assertEqual((s.format, s.size), ('hhi', struct.calcsize('hhi')))
        self.assertEqual(s.pack(1, 2, 3), struct.pack('hhi', 1, 2, 3))
        self.assertEqual(s.pack_into(bytearray(10), 3, 1, 2, 3),
                         struct.pack_into(bytearray(10), 3, 'hhi', 1, 2, 3))
        self.assertEqual(s.pack_into(bytearray(10), 3, 1, 2, 3), 3)
        self.assertEqual(s.unpack(b'\x01\x00\x02\x00\x03\x00\x04\x00'),
                         (1, 2, 3))
        self
