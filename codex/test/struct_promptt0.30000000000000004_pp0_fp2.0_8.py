import _struct
# Test _struct.Struct

class StructTest(unittest.TestCase):

    def test_struct_unpack(self):
        # Test the unpack method of Struct objects
        s = _struct.Struct('i')
        self.assertEqual(s.unpack(b'abcd'), (1633837924,))
        self.assertEqual(s.unpack(b'efgh'), (1701074259,))
        self.assertRaises(TypeError, s.unpack, 'abcdefgh')
        self.assertRaises(TypeError, s.unpack, memoryview(b'abcdefgh'))
        self.assertRaises(TypeError, s.unpack, bytearray(b'abcdefgh'))
        self.assertRaises(TypeError, s.unpack, array.array('b', b'abcdefgh'))
        self.assertRaises(TypeError, s.unpack, array.array('B', b'abcdefgh'))
