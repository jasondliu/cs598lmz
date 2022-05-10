import _struct
# Test _struct.Struct
class StructTest(unittest.TestCase):
    def test_unpack_from(self):
        s = _struct.Struct('>i')
        buf = array.array('b', [0, 0, 0, 1])
        self.assertEqual(s.unpack_from(buf), (1,))
        self.assertEqual(s.unpack_from(buf, 1), (16777216,))
        self.assertEqual(s.unpack_from(buf, 1, 2), (16777216,))
        self.assertEqual(s.unpack_from(buf, 1, 1), (4194304,))
        self.assertEqual(s.unpack_from(buf, 1, 0), (0,))
        self.assertRaises(ValueError, s.unpack_from, buf, 1, 3)
        self.assertRaises(ValueError, s.unpack_from, buf, 1, 4)
        self.assertRaises(ValueError, s.unpack_from, buf, 1, 5)
       
