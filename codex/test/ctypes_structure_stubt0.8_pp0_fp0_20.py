import ctypes

class S(ctypes.Structure):
    x = (1,2,3)

class E(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class F(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class G(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

def test_subclasses():
    assert ctypes.Structure.__subclasses__() == [E, F, G]

