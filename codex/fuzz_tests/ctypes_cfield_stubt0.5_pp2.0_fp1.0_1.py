import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

CField = ctypes.CField

class Test(unittest.TestCase):
    def test_field_type(self):
        self.assertEqual(type(C.x), CField)
        self.assertEqual(type(D.x), CField)
        self.assertEqual(type(S.x), CField)

    def test_field_name(self):
        self.assertEqual(C.x.name, "x")
        self.assertEqual(D.x.name, "x")
        self.assertEqual(S.x.name, "x")

    def test_field_type_name(self):
        self.assertEqual(C.x.ctype.__name__, "c_int")
        self.assertEqual(D.x.ctype.__name
