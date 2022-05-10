import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFieldTest(unittest.TestCase):
    def test_type(self):
        self.assertEqual(type(S.x), ctypes.CField)

    def test_repr(self):
        self.assertEqual(repr(S.x), "CField('x', c_int, <field offset 0>)")

    def test_get(self):
        s = S(42)
        self.assertEqual(s.x, 42)

    def test_set(self):
        s = S(0)
        s.x = 42
        self.assertEqual(s.x, 42)

    def test_set_wrong_type(self):
        s = S(0)
        with self.assertRaises(TypeError):
            s.x = "hello"

    def test_get_from_pointer(self):
        s = S(42)
        self.assertEqual(ctypes.cast(id(s), ctypes.POINTER(S)).contents.x, 42)

    def test_set_
