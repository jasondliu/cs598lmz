import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class D(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int)]


class E(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int)]

class F(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.POINTER(E))]

class G(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.POINTER(F))]

class H(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.POINTER(G))]

class Test(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(S._fields_, [("x", ctypes.c_int)])
        self.failUnless(isinstance(S._fields
