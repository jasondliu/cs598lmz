import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, x):
        self.x = x

def f(x):
    return x

class Test(unittest.TestCase):
    def test_cfield(self):
        self.assertEqual(ctypes.CField, type(S.x))
        self.assertEqual(ctypes.CField, type(C.x))
        self.assertEqual(ctypes.CField, type(f.__code__))

    def test_cfield_name(self):
        self.assertEqual(S.x.name, 'x')
        self.assertEqual(C.x.name, 'x')
        self.assertEqual(f.__code__.name, 'f')

    def test_cfield_type(self):
        self.assertEqual(S.x.type, ctypes.c_int)
        self.assertEqual(C.x.type, int)
        self.assertEqual(f.__code__.type, type(f.__
