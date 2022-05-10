import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(ctypes.CField, type(S.x))
        self.assertEqual(ctypes.CField, type(ctypes.c_int))
        self.assertEqual(ctypes.CField, type(ctypes.c_byte))

    def test_subclass(self):
        class X(ctypes.CField):
            pass
        self.assertEqual(X, type(X()))

    def test_get_name(self):
        self.assertEqual(S.x.__name__, 'x')
        self.assertEqual(S.x.name, 'x')

    def test_get_type(self):
        self.assertEqual(S.x.__type__, ctypes.c_int)
        self.assertEqual(S.x.type, ctypes.c_int)
        self.assertEqual(type(S.x.type), ctypes.CField)

    def test_
