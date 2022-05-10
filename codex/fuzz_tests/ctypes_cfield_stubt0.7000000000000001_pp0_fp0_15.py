import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x) # for compatibility with Python 2.6

class test_CField(unittest.TestCase):
    def test_get_set(self):
        s = S()
        self.assertEqual(s.x, 0)
        s.x = 42
        self.assertEqual(s.x, 42)
        s.x = -1
        self.assertEqual(s.x, -1)

    def test_invalid_assignment(self):
        s = S()
        def assign(value): s.x = value
        self.assertRaises(ValueError, assign, 'x')
        self.assertRaises(TypeError, assign, 1.5)

    def test_from_address(self):
        s = S()
        addr = ctypes.addressof(s)
        field = ctypes.Field('x', ctypes.c_int, addr)
        self.assertEqual(s.x, 0)
        field.value = 42
        self.assertEqual(s.x, 42)
        s.x = -1
