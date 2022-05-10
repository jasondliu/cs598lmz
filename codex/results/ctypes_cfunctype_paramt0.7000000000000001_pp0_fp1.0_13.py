import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,
                           ctypes.c_int,
                           ctypes.c_int)

class C(object):
    def __init__(self, x=0):
        self.x = x
    def f(self, a, b):
        return a + b + self.x

def g(a, b):
    return a+b

class TestCallbacks(unittest.TestCase):
    def test1(self):
        obj = C(100)
        cptr = FUNTYPE(obj.f)
        self.assertEqual(cptr(1, 2), 103)
        cptr = FUNTYPE(g)
        self.assertEqual(cptr(1, 2), 3)
        cptr = FUNTYPE(lambda a,b: a+b+1000)
        self.assertEqual(cptr(1, 2), 1003)
        #
        cptr = FUNTYPE(obj.f)
        cptr.__self__ = None
        self.assertRaises(TypeError, cptr, 1, 2
