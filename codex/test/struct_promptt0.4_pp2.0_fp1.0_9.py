import _struct
# Test _struct.Struct

from test import support

from _struct import Struct as _Struct

# Test _Struct.__new__
class StructTest(unittest.TestCase):

    def test_new(self):
        # Test _Struct.__new__
        self.assertRaises(TypeError, _Struct)
        self.assertRaises(TypeError, _Struct, 'abc', 1)
        self.assertRaises(TypeError, _Struct, 'abc', 1, 2, 3)
        self.assertRaises(TypeError, _Struct, 'abc', 1, 2, 3, 4)
        self.assertRaises(TypeError, _Struct, 'abc', 1, 2, 3, 4, 5)
        self.assertRaises(TypeError, _Struct, 'abc', 1, 2, 3, 4, 5, 6)
        self.assertRaises(TypeError, _Struct, 'abc', 1, 2, 3, 4, 5, 6, 7)
