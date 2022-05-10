import _struct
# Test _struct.Struct.
class StructTest(unittest.TestCase):
    def test_simple_types(self):
        s = _struct.Struct('c')
        self.assertEqual(s.size, 1)
        self.assertEqual(s.pack_into(bytes(1), 0, b'A'), None)
        self.assertEqual(s.unpack_from(b'A'), (b'A',))
        s = _struct.Struct('b')
        self.assertEqual(s.size, 1)
        self.assertEqual(s.pack_into(bytes(1), 0, 2**7-1), None)
        self.assertEqual(s.unpack_from(bytes([2**7-1])), (2**7-1,))
        self.assertEqual(s.pack_into(bytes(1), 0, -1), None)
        self.assertEqual(s.unpack_from(bytes([255])), (-1,))
        s = _struct.Struct('B')
