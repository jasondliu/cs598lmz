import _struct
# Test _struct.Struct
from test import support

class StructTest(unittest.TestCase):

    def test_Struct(self):
        ints = (1, 2)
        s = _struct.Struct('hh')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(*ints), b'\x01\x00\x02\x00')
        self.assertEqual(s.unpack(s.pack(*ints)), ints)
        self.assertEqual(s.pack_into(bytearray(s.size), 0, *ints), None)
        self.assertEqual(s.unpack_from(s.pack(*ints), 0), ints)
        self.assertEqual(s.unpack_from(bytearray(s.pack(*ints)), 0), ints)
        self.assertEqual(s.unpack(s.pack(*ints)), ints)
        self.assertEqual(s.unpack_from(s.pack(*ints), 0), ints)
        self.assertEqual(
