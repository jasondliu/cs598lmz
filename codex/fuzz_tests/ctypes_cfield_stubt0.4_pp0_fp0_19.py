import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):

    def test_field_type(self):
        self.assertEqual(type(S.x), ctypes.CField)

    def test_field_name(self):
        self.assertEqual(S.x.name, "x")

    def test_field_offset(self):
        self.assertEqual(S.x.offset, 0)

    def test_field_ctype(self):
        self.assertEqual(S.x.ctype, ctypes.c_int)

    def test_field_size(self):
        self.assertEqual(S.x.size, ctypes.sizeof(ctypes.c_int))

    def test_field_from_address(self):
        s = S()
        self.assertEqual(ctypes.CField.from_address(ctypes.addressof(s), ctypes.c_int), S.x)

    def test_field_from_address_with_offset(self):
        s = S()
        self.assert
