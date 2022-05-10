import _struct
# Test _struct.Struct.__repr__
#
# Test _struct.Struct.__reduce__
#
# Test _struct.Struct.__reduce_ex__
#
# Test _struct.Struct.__setstate__

class StructTestCase(unittest.TestCase):

    def test_error_reporting(self):
        self.assertRaises(TypeError, _struct.Struct, 'abc')
        self.assertRaises(TypeError, _struct.Struct, b'abc')
        self.assertRaises(TypeError, _struct.Struct, 'abc', '=')
        self.assertRaises(TypeError, _struct.Struct, 'abc', '=', True)
        self.assertRaises(TypeError, _struct.Struct, 'abc', '=', False)
        self.assertRaises(TypeError, _struct.Struct, 'abc', '=', None)
        self.assertRaises(TypeError, _struct.Struct, 'abc', '=', (1, 2, 3))
