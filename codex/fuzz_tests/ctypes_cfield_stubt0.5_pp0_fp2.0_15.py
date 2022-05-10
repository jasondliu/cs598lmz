import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class F(ctypes.c_int):
    pass

class Test(unittest.TestCase):
    def test_cfield(self):
        self.assertEqual(type(S.x), ctypes.CField)

    def test_c_int(self):
        x = ctypes.c_int()
        self.assertRaises(TypeError, ctypes.c_int, "42")
        self.assertRaises(TypeError, ctypes.c_int, 42.0)
        self.assertRaises(TypeError, ctypes.c_int, None)
        self.assertEqual(x.value, 0)
        x.value = 42
        self.assertEqual(x.value, 42)
        x.value = "42"
        self.assertEqual(x.value, 42)
        x.value = 42.0
        self.assertEqual(x.value, 42)
        x.value = None
        self.assertEqual(x.value, 0)

    def test_c_int_subclass
