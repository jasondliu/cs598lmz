import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):

    def test_getter(self):
        obj = S()
        self.assertEqual(obj.x, 0)
        obj.x = 42
        self.assertEqual(obj.x, 42)

    def test_setter(self):
        obj = S()
        obj.x = 1
        self.assertEqual(obj.x, 1)
        obj.x = 42
        self.assertEqual(obj.x, 42)

    def test_setter_wrong_type(self):
        obj = S()
        with self.assertRaises(TypeError):
            obj.x = 'hello'

    def test_setter_wrong_value(self):
        obj = S()
        with self.assertRaises(ValueError):
            obj.x = -1

    def test_get_sizeof(self):
        self.assertEqual(ctypes.sizeof(S), ctypes.sizeof(S.x))

    def test_get_alignment(self):
        self
