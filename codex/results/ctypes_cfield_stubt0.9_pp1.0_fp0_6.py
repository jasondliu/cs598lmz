import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CFieldType = type(S.x.__class__)

class Test_CField_PyObject(unittest.TestCase):
    def test_CField_repr(self):
        self.assertEqual(repr(S.x),
                         "<CField type 'c_int' of 'S' structures>")

    def test_CField_class(self):
        self.assertEqual(S.x.__class__, ctypes.CField)
        self.assertEqual(type(S.x), ctypes.CField)

    def test_CField_type(self):
        self.assertEqual(type(S.x.type), ctypes.CFieldType)
        self.assertEqual(type(S.x.type), type(S.x.__class__))

    def test_CField_fieldtype_repr(self):
        self.assertEqual(repr(S.x.type),
                         "<CFieldType 'c_int'>")

    def test_CField_len(self):

