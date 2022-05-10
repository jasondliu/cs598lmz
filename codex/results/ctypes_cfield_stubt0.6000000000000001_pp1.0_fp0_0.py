import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFieldTest(unittest.TestCase):

    def test_create_cfield_with_int(self):
        self.assertEqual(ctypes.CField(ctypes.c_int),
                         ctypes.c_int)

    def test_create_cfield_with_str(self):
        self.assertEqual(ctypes.CField("i"),
                         ctypes.c_int)

    def test_create_cfield_with_type(self):
        self.assertEqual(ctypes.CField(ctypes.c_int),
                         ctypes.c_int)

    def test_create_cfield_with_other(self):
        with self.assertRaises(TypeError) as cm:
            ctypes.CField(S())
        self.assertEqual(str(cm.exception),
                         "expected a type, string, or CField instance")

    def test_create_cfield_without_args(self):
        with self.assertRaises(TypeError) as cm:
            ctypes.CField
