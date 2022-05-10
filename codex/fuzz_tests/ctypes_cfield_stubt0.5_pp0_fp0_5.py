import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):
    def test_cfield_repr(self):
        self.assertEqual(repr(S.x), '<CField type=c_int, offset=0>')

    def test_cfield_set_get(self):
        s = S()
        self.assertEqual(s.x, 0)
        s.x = 42
        self.assertEqual(s.x, 42)

    def test_cfield_set_get_typeerror(self):
        s = S()
        self.assertRaises(TypeError, setattr, s, 'x', '42')
        self.assertRaises(TypeError, setattr, s, 'x', 42.0)
        self.assertRaises(TypeError, setattr, s, 'x', None)

    def test_cfield_set_get_overflow(self):
        s = S()
        self.assertRaises(OverflowError, setattr, s, 'x', 2**32)
        self.assertRaises(Over
