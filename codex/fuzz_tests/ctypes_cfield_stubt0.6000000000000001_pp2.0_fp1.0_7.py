import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):
    def test_cfield_type(self):
        self.assertIs(type(S.x), ctypes.CField)

    def test_cfield_name(self):
        self.assertEqual(S.x.name, 'x')

    def test_cfield_ctype(self):
        self.assertIs(S.x.ctype, ctypes.c_int)

    def test_cfield_offset(self):
        self.assertEqual(S.x.offset, 0)

    def test_cfield_size(self):
        self.assertEqual(S.x.size, 4)

    def test_cfield_alignment(self):
        self.assertEqual(S.x.alignment, 4)

    def test_cfield_get(self):
        s = S()
        s.x = 42
        self.assertEqual(S.x.get(s), 42)

    def test_cfield_set(self):
        s = S()
       
