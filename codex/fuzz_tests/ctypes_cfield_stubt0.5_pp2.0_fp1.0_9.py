import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(ctypes.CField(ctypes.c_int).__name__, 'x')

    def test_repr(self):
        self.assertEqual(repr(ctypes.CField(ctypes.c_int)),
                         "<CField 'x' of type 'c_int'>")

    def test_type(self):
        self.assertEqual(ctypes.CField(ctypes.c_int).type, ctypes.c_int)

    def test_from_address(self):
        s = S(42)
        self.assertEqual(ctypes.CField.from_address(id(s)).__name__, 'x')

    def test_from_address_fail(self):
        self.assertRaises(TypeError, ctypes.CField.from_address, 'foo')

    def test_offset(self):
        self.assertEqual(ctypes.CField(ctypes.c_int).offset,
