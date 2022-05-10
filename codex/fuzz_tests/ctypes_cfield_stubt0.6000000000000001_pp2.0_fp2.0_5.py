import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):

    def test_c_int(self):
        self.assertEqual(S.x.__class__, ctypes.CField)
        self.assertEqual(S.x.type, ctypes.c_int)
        self.assertEqual(S.x.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(S.x.offset, ctypes.offsetof(S, "x"))
        self.assertEqual(S.x.name, "x")
        self.assertEqual(S.x.index, 0)
        self.assertEqual(S.x.pack, 1)

    def test_c_int_array(self):
        class S(ctypes.Structure):
            _fields_ = [('x', ctypes.c_int * 5)]

        self.assertEqual(S.x.__class__, ctypes.CField)
        self.assertEqual(S.x.type, ctypes.c_int * 5)
