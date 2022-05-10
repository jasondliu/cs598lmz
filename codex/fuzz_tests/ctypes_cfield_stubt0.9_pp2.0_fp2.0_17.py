import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFieldTest(unittest.TestCase):
    def test_getattr(self):
        self.assertRaises(AttributeError, getattr, S.x, 'foo')
        self.assertEqual(getattr(S.x, 'offset'), 0)
        self.assertEqual(getattr(S.x, 'ctype'), ctypes.c_int)

    @unittest.skipUnless(hasattr(S.x, '__setattr__'), 'Requires Python >= 2.6')
    def test_setattr(self):
        x = S.x
        self.assertRaises(TypeError, setattr, x, 'offset', 0)
        self.assertRaises(TypeError, setattr, x, 'ctype', ctypes.c_int)


if __name__ == "__main__":
    unittest.main()
