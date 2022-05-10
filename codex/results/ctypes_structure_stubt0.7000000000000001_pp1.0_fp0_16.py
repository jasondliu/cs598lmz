import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longdouble()

class U(ctypes.Union):
    x = ctypes.c_longdouble()
    y = ctypes.c_int()

class Test(unittest.TestCase):
    def test_longdouble(self):
        for T in S, U:
            v = T()
            v.x = 123.456
            self.assertEqual(v.x, 123.456)
            self.assertEqual(sys.getsizeof(v), ctypes.sizeof(ctypes.c_longdouble))

    def test_default_shortened(self):
        # default is float, not double
        self.assertEqual(ctypes.c_longdouble(123), 123.0)
        self.assertEqual(ctypes.c_longdouble(123.0), 123.0)
        self.assertEqual(ctypes.c_longdouble(123.0).value, 123.0)

    def test_longdouble_from_double(self):
        # converting from a double to longdouble shouldn't be shortened

