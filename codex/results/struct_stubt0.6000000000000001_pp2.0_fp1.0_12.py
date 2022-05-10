from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>hhl'
s.size = 8

def get_packed_data():
    """Return the byte string used in the test."""
    return pack('>hhl', 1, 2, 3)

class StrTest(unittest.TestCase):
    def test_iter(self):
        self.assertEqual(list(iter(s)), [('x', 'h', 1), ('y', 'h', 2), ('z', 'l', 3)])

    def test_size(self):
        self.assertEqual(s.size, 8)

    def test_pack(self):
        self.assertEqual(s.pack(1, 2, 3), get_packed_data())

    def test_unpack(self):
        self.assertEqual(s.unpack(get_packed_data()), (1, 2, 3))

    def test_pack_into(self):
        buf = bytearray(b'12345678')
        s.pack_into(buf, 1, 1, 2, 3)
        self
