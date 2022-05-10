import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):
    def test_type(self):
        self.assertTrue(type(S.x) is ctypes.CField)

    def test_immutable(self):
        self.assertRaises(AttributeError, setattr, S.x, 'x', 3)

    def test_contains(self):
        self.assertTrue(ctypes.CField('x') in [ctypes.CField('x')])

if __name__ == '__main__':
    unittest.main()
