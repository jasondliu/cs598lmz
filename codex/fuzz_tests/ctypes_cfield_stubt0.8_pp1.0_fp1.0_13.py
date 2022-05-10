import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CArrayType = type(ctypes.c_char * 4)
ctypes.CFieldArrayType = type(S.x * 1)

class StructField_TestCase(unittest.TestCase):
    def test_field(self):
        self.assertEqual(S.x.offset, 0)
        self.assertIs(S.x.ctype, ctypes.c_int)
        self.assertIs(S.x.of_type, ctypes.Structure)
        self.assertEqual(S.x.name, "x")
        self.assertEqual(S.x.pack_for(S), 1)

    def test_subclass(self):
        # Issue 8151: ctypes.Structure.__subclasscheck__
        # should not raise a TypeError for subfields
        self.assertTrue(issubclass(S.x.__class__, ctypes.CField))
        self.assertFalse(issubclass(S.x.__class__, ctypes.CArrayType))

    def test_subclass_
