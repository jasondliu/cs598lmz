import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):
    def test(self):
        s = S()
        self.assertEqual(s.x, 0)
        self.assertEqual(s._fields_[0][1].size, 4)

    def test_type(self):
        self.assertEqual(S.x.__class__, ctypes.CField)

    def test_from_param(self):
        self.assertEqual(S.x.from_param(S.x), S.x)

    def test_from_address(self):
        self.assertEqual(S.x.from_address(id(S.x)), S.x)

    def test_set(self):
        S.x = 5
        self.assertEqual(S.x, 5)

    def test_set_struct(self):
        s = S()
        s.x = 5
        self.assertEqual(s.x, 5)

    def test_set_bad(self):
        s = S()
        self.assertRaises
