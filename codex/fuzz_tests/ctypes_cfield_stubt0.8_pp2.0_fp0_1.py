import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_CField_get_name(self):
    self.assertEqual(S.x.name, 'x')

def test_CField_get_offset(self):
    self.assertEqual(S.x.offset, ctypes.addressof(S().x) - ctypes.addressof(S()))

def test_CField_get_size(self):
    self.assertEqual(S.x.size, ctypes.sizeof(S().x))

if __name__ == "__main__":
    unittest.main()
