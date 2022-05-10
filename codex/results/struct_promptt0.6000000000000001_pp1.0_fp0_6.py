import _struct
# Test _struct.Struct.
# (see issue #18205)

class StructTest(unittest.TestCase):

    def test_struct(self):
        # test basic packing and unpacking
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(1), b'\x01\x00\x00\x00')
        self.assertRaises(TypeError, s.pack, 'abc')
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertRaises(TypeError, s.unpack, 'abc')

    def test_iter(self):
        # test packing and unpacking from iterables
        s = _struct.Struct('2i')
        self.assertEqual(s.size, 8)
        self.assertEqual(s.pack(1, 2), b'\x01\x00\x00\x00\x02\x00\x00\x00')
        self
