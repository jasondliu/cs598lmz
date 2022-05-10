import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):
    def test_struct_field(self):
        s = S(42)
        self.assertEqual(s.x, 42)
        s.x = 24
        self.assertEqual(s.x, 24)

    def test_field_type(self):
        self.assertIs(type(S.x), ctypes.CField)

    def test_field_name(self):
        self.assertEqual(S.x.name, 'x')

    def test_field_ctype(self):
        self.assertIs(S.x.ctype, ctypes.c_int)

    def test_field_offset(self):
        self.assertEqual(S.x.offset, 0)

    def test_field_size(self):
        self.assertEqual(S.x.size, ctypes.sizeof(ctypes.c_int))

    def test_field_bits(self):
        self.assertEqual(S.x.bits, ctypes.sizeof(ctypes
