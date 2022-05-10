import _struct
# Test _struct.Struct

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        # Test _struct.Struct
        s = _struct.Struct('i')
        self.assertEqual(s.size, _struct.calcsize('i'))
        self.assertRaises(TypeError, s.pack, 'hi')
        self.assertRaises(TypeError, s.pack, 1, 2)
        self.assertRaises(TypeError, s.pack, 1.0)
        self.assertRaises(TypeError, s.pack, None)
        self.assertRaises(TypeError, s.pack, [1])
        self.assertRaises(TypeError, s.pack, (1,))
        self.assertRaises(TypeError, s.pack, {1:1})
        self.assertRaises(TypeError, s.pack)
        self.assertRaises(TypeError, s.pack, 1, 2, 3)
        self.assertRaises(TypeError, s.pack, 1, 2, 3, 4)
        self
