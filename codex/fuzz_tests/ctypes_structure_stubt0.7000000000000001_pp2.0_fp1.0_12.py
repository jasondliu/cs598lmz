import ctypes

class S(ctypes.Structure):
    x = ctypes.Structure.x

class S2(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

class C(object):
    x = 123

class D(C, ctypes.Structure):
    _fields_ = [("y", ctypes.c_int)]

class E(ctypes.Structure, C):
    _fields_ = [("y", ctypes.c_int)]

class F(D, E):
    _fields_ = [("z", ctypes.c_int)]

class G(E, D):
    _fields_ = [("z", ctypes.c_int)]

class Test(unittest.TestCase):
    def test_1(self):
        self.assertRaises(AttributeError, S)
        self.assertRaises(AttributeError, S2)

    def test_2(self):
        self.assertRaises(AttributeError, S().__setattr__, "x", 42)

    def test_3(self):
        self.assertE
