import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):
    def test_init(self):
        self.assertEqual(S(x=42).x, 42)

    def test_get(self):
        self.assertEqual(S().x, 0)
        self.assertEqual(S(x=42).x, 42)

    def test_set(self):
        s = S()
        s.x = 42
        self.assertEqual(s.x, 42)

    def test_set_invalid(self):
        s = S()
        try:
            s.x = "hello"
        except TypeError:
            pass
        else:
            self.fail("setting a string should have raised TypeError")

    def test_from_param(self):
        self.assertEqual(
            ctypes.c_int.from_param(S(x=42)),
            42
        )

    def test_from_address(self):
        s = S(x=42)
        a = ctypes.addressof(s)
       
