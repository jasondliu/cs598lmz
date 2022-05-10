import _struct
# Test _struct.Struct.__new__
class TestStructNew(unittest.TestCase):
    def test_bad_fmt(self):
        self.assertRaises(TypeError, _struct.Struct, 'i'.encode())
        self.assertRaises(TypeError, _struct.Struct, 1)
        self.assertRaises(TypeError, _struct.Struct, None)
        self.assertRaises(TypeError, _struct.Struct)

    def test_bad_fmt(self):
        self.assertRaises(TypeError, _struct.Struct, 'QQQQQQQQQQQQ')
        self.assertRaises(TypeError, _struct.Struct, 'Q' * (1 << 32))


# Test _struct.Struct.__repr__
