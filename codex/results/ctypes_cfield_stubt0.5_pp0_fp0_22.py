import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):
    def test_c_field(self):
        self.assertEqual(ctypes.CField.__name__, "CField")
        self.assertEqual(ctypes.CField.__module__, "ctypes")

    def test_type(self):
        self.assertEqual(type(S.x), ctypes.CField)

    def test_get(self):
        self.assertEqual(S.x, S._fields_[0])

    def test_set(self):
        self.assertRaises(TypeError, setattr, S.x, "name", "x")
        self.assertRaises(TypeError, setattr, S.x, "type", ctypes.c_char)
        self.assertRaises(TypeError, setattr, S.x, "offset", 0)
        self.assertRaises(TypeError, setattr, S.x, "from_address", None)
        self.assertRaises(TypeError, setattr, S.x, "__dict__
