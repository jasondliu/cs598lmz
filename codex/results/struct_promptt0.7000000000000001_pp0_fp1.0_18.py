import _struct
# Test _struct.Struct
class StructTest(unittest.TestCase):
    def test_bad_format(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, b'', 0)
        self.assertRaises(TypeError, _struct.Struct, b'{')
        self.assertRaises(TypeError, _struct.Struct, b'}')
        self.assertRaises(TypeError, _struct.Struct, b' ')
        self.assertRaises(TypeError, _struct.Struct, b'@ ')
        self.assertRaises(TypeError, _struct.Struct, b'x')
        self.assertRaises(TypeError, _struct.Struct, b'@x')
        self.assertRaises(TypeError, _struct.Struct, b'@xi')
        self.assertRaises(TypeError, _struct.Struct, b'@i x')
        self.assertRaises(TypeError, _struct.Struct, b'@ix', 0)
        self.assertRaises(
