import _struct
# Test _struct.Struct
class StructTestCase(unittest.TestCase):
    def test_struct(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(42), b'*\x00\x00\x00')
        self.assertEqual(s.unpack(b'*\x00\x00\x00'), (42,))
        self.assertEqual(s.unpack(array.array('b', b'*\x00\x00\x00')), (42,))
        self.assertRaises(TypeError, s.pack, 'foo')
        self.assertRaises(TypeError, s.pack, 1, 2)
        self.assertRaises(TypeError, s.unpack, 'foo')
        self.assertRaises(TypeError, s.unpack, b'foo', 'bar')
