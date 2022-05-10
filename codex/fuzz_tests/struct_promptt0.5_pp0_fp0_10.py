import _struct
# Test _struct.Struct

class StructTestCase(unittest.TestCase):
    def test_integers(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(42), b'*\x00\x00\x00')
        self.assertEqual(s.unpack(b'*\x00\x00\x00'), (42,))
        self.assertEqual(s.unpack_from(b'\x00'*4 + b'*\x00\x00\x00'), (42,))
        self.assertEqual(s.pack_into(bytearray(b'\x00'*4), 0, 42), None)
        self.assertEqual(bytes(bytearray(b'\x00'*4)), b'*\x00\x00\x00')

    def test_floats(self):
        s = _struct.Struct('d')
        self.assertEqual(s.size, 8)
        self
