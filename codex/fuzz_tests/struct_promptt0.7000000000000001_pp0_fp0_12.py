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
class TestStructRepr(unittest.TestCase):
    def test_repr(self):
        for fmt in ('x', 'b', 'h', 'i', 'l', 'q', 'B', 'H', 'I', 'L', 'Q',
                    'f', 'd'):
           
