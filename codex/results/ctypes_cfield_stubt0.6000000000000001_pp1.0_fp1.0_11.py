import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(C):
    _fields_ = [('y', ctypes.c_int)]

class E(D):
    _fields_ = [('z', ctypes.c_int)]

class F(D):
    _fields_ = [('z', ctypes.c_int)]

class G(D):
    _fields_ = [('w', ctypes.c_int)]

class Test(unittest.TestCase):

    def test_field_attr(self):
        self.assertEqual(S.x.offset, 0)
        self.assertEqual(S.x.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(S.x.name, 'x')
        self.assertEqual(S.x.ctype, ctypes.c_int)
        self.assertEqual(S.x.index, 0)

    def test_field_attr_in
