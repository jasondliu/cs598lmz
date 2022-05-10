import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):

    def test_cfield(self):
        self.assertEqual(S.x.__class__, ctypes.CField)

    def test_cfield_name(self):
        self.assertEqual(S.x.name, 'x')

    def test_cfield_ctype(self):
        self.assertEqual(S.x.ctype, ctypes.c_int)

    def test_cfield_offset(self):
        self.assertEqual(S.x.offset, 0)

    def test_cfield_index(self):
        self.assertEqual(S.x.index, 0)

    def test_cfield_from_param(self):
        self.assertEqual(S.x.from_param(None), None)

    def test_cfield_from_param_value(self):
        self.assertEqual(S.x.from_param(0), 0)

    def test_cfield_from_param_value_error(self):
        self
