import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):
    def test_c_field(self):
        p = ctypes.POINTER(ctypes.c_int)
        self.assertEqual(p._type_, ctypes.c_int)

    def test_ptr_field(self):
        p = ctypes.POINTER(S)
        self.assertEqual(p._type_, S)

    def test_c_field_type(self):
        self.assertEqual(ctypes.c_int._type_, ctypes.c_int)

    def test_c_void_p_type(self):
        self.assertEqual(ctypes.c_void_p._type_, ctypes.c_void_p)

    def test_c_char_p_type(self):
        self.assertEqual(ctypes.c_char_p._type_, ctypes.c_char_p)

    def test_pointer_type(self):
        p = ctypes.POINTER(ctypes.c_int)
        self
