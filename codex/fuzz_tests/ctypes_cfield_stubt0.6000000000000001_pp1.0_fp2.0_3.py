import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):
    def test_cfield(self):
        self.assertEqual(type(S.x), ctypes.CField)

    def test_cfield_repr(self):
        self.assertEqual(repr(S.x), "<CField 'x' of type c_int at %s>" % hex(id(S.x)))

    def test_cfield_type(self):
        self.assertEqual(S.x.type, ctypes.c_int)

    def test_cfield_name(self):
        self.assertEqual(S.x.name, 'x')

    def test_cfield_offset(self):
        self.assertEqual(S.x.offset, ctypes.sizeof(ctypes.c_int))

    def test_cfield_from_address(self):
        self.assertEqual(ctypes.CField.from_address(id(S.x)).name, 'x')


if __name__ == "__main__":
    unittest
