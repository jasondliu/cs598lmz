import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int)]

def test_cfield_from_address(self):
    p = ctypes.pointer(S())
    self.assertEqual(p.contents.x, 0)
    self.assertEqual(ctypes.c_int.from_address(id(p.contents.x)).value, 0)
    p.contents.x = 1
    self.assertEqual(ctypes.c_int.from_address(id(p.contents.x)).value, 1)
    p = None
    self.assertRaises(ValueError, ctypes.c_int.from_address, id(p.contents.x))

def test_cfield_from_buffer(self):
    p = ctypes.pointer(S2())
    self.assertEqual(p.contents.x, 0)
    self.assertEqual
