import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"

def f(x):
    return x*x

def f2(x,y):
    return x*y

def f3(x,y,z):
    return x*y*z

def f4(x,y,z,w):
    return x*y*z*w

class TestCtypes(TestCase):
    def test_funtype(self):
        self.assertEqual(fun(), "Hello")
        self.assertEqual(fun, fun())

    def test_funtype_args(self):
        fun2 = FUNTYPE(lambda x: x*x)
        self.assertEqual(fun2(2), 4)

    def test_funtype_args_many(self):
        fun2 = FUNTYPE(lambda x,y,z,w: x*y*z*w)
        self.assertEqual(fun2(1,2,3,4), 24)

    def test_funtype_args_many2(self):
        fun2 = FUNTYPE(lambda x,y,z:
