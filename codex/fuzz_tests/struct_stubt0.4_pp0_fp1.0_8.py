from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<2si'
s.size = 8

class StructTestCase(unittest.TestCase):
    def test_unpack(self):
        values = (1, 2, 3)
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00\x02\x00\x00\x00'), values)
        self.assertEqual(s.unpack_from(b'\x01\x00\x00\x00\x02\x00\x00\x00', 0), values)
        self.assertEqual(s.unpack_from(b'\x01\x00\x00\x00\x02\x00\x00\x00', 1), (0, 2, 3))
        self.assertEqual(s.unpack_from(b'\x01\x00\x00\x00\x02\x00\x00\x00', 2), (0, 0, 3))
        self.assertEqual(s.unpack_from
