import _struct
# Test _struct.Struct

class StructTest(unittest.TestCase):
    def test_struct_unpack(self):
        s = _struct.Struct("ii")
        self.assertEqual(s.unpack(b"\0\0\0\0\0\0\0\0"), (0, 0))
        self.assertEqual(s.unpack(b"\0\0\0\0\0\0\0\1"), (0, 1))
        self.assertEqual(s.unpack(b"\1\0\0\0\0\0\0\0"), (1, 0))
        self.assertEqual(s.unpack(b"\1\0\0\0\1\0\0\0"), (1, 1))
        self.assertEqual(s.unpack(b"\1\0\0\0\1\0\0\0"), (1, 1))
        self.assertEqual(s.unpack(b"\1\0\0\0\1\0\0\0"), (1,
