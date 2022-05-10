import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CField_test(unittest.TestCase):
    def test_base(self):
        self.assertEqual(S.x.offset, 0)
        self.assertEqual(S.x.size, 4)
        self.assertEqual(S.x.index, 0)
        self.assertEqual(S.x.pack, 1)
        self.assertEqual(S.x.ctype, ctypes.c_int)
        self.assertEqual(S.x.name, 'x')
        self.assertEqual(S.x.type, ctypes.c_int)

        self.assertEqual(repr(S.x), "CField(('x', <class 'ctypes.c_int'>))")

    def test_repr(self):
        self.assertEqual(repr(S.x), "CField(('x', <class 'ctypes.c_int'>))")

    def test_hash(self):
        self.assertEqual(hash(S.x), hash(('x', c
