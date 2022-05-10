import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Fields(ctypes.Structure):
    pass

class T(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.POINTER(Fields))]

class X(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.POINTER(T))]

class Test_fields(unittest.TestCase):
    def test_simple(self):
        s = S()
        s.x = 42
        self.assertEqual(s.x, 42)
        self.assertEqual(s._fields_[0], ('x', ctypes.c_int))

        self.assertEqual(S._fields_, [('x', ctypes.c_int)])
        S._fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
        self.assertEqual(S._fields_, [('x', ctypes.c_int), ('y', c
