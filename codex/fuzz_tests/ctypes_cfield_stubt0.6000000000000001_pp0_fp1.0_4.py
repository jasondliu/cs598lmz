import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):

    def test_cfield(self):
        s = S()
        self.assertEqual(s.x, 0)
        s.x = 42
        self.assertEqual(s.x, 42)
        self.assertRaises(TypeError, setattr, s, 'x', "hello")
        self.assertRaises(TypeError, setattr, s, 'x', 42.0)
        self.assertRaises(TypeError, setattr, s, 'x', 42.5)
        self.assertRaises(TypeError, setattr, s, 'x', True)
        self.assertRaises(TypeError, setattr, s, 'x', 2**100)
        self.assertRaises(TypeError, setattr, s, 'x', -2**100)

        # test the repr() of CField
        self.assertEqual(repr(S.x), "CField(c_int, 'x')")

    def test_cfield_of_cfield(self):
        class S
