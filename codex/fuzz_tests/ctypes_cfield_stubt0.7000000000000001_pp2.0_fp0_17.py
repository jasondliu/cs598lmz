import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(S.x.offset, 0)
        self.assertEqual(S.x.size, 4)
        self.assertEqual(S.x.index, 0)

    def test_argtypes(self):
        self.assertEqual(ctypes.c_byte.argtypes, (ctypes.c_byte,))
        self.assertEqual(ctypes.c_short.argtypes, (ctypes.c_short,))
        self.assertEqual(ctypes.c_int.argtypes, (ctypes.c_int,))
        self.assertEqual(ctypes.c_long.argtypes, (ctypes.c_long,))
        self.assertEqual(ctypes.c_longlong.argtypes, (ctypes.c_longlong,))

        self.assertEqual(ctypes.c_ubyte.argtypes, (ctypes.c_ubyte,))
        self.assertEqual(
