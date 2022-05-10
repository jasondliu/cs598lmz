import _struct
# Test _struct.Struct
Struct = _struct.Struct

todo = 'pack unpack size'.split()

class TestBasic(unittest.TestCase):
    def test_new_names(self):
        # check invalid names
        self.assertRaises(ValueError, _struct.Struct, 'A')
        self.assertRaises(ValueError, _struct.Struct, 'Z')
        self.assertRaises(ValueError, _struct.Struct, 'abc\x00def')
        self.assertRaises(ValueError, _struct.Struct, 'abc\u0100def')
        self.assertRaises(ValueError, _struct.Struct, 'ab<cd')
        self.assertRaises(ValueError, _struct.Struct, 'ab>cd')
        self.assertRaises(ValueError, _struct.Struct, 'ab@cd')
        self.assertRaises(ValueError, _struct.Struct, 'x' * 1000)
        # check valid names without '=' or '!' at the end
        self.assertEqual(_struct.Struct('abcdefgh').format, 'abcdefgh
