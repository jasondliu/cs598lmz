import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield(self):
    self.assertEqual(type(S.x), ctypes.CField)
    self.assertEqual(S.x.__name__, 'x')
    self.assertEqual(S.x.offset, ctypes.sizeof(ctypes.c_int))
    self.assertEqual(S.x.size, ctypes.sizeof(ctypes.c_int))
    self.assertEqual(S.x.index, 0)
    self.assertEqual(S.x.ctype, ctypes.c_int)
    self.assertEqual(S.x.type, ctypes.c_int)

if __name__ == "__main__":
    unittest.main()
