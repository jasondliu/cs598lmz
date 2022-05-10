import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X:
    def __init__(self, x):
        self.x = x

class Y:
    def __init__(self, x):
        self.x = x

class Z:
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return self.x == other.x
    def __ne__(self, other):
        return self.x != other.x

class W(object):
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return self.x == other.x
    def __ne__(self, other):
        return self.x != other.x

class V(object):
    def __init__(self, x):
        self.x = x
    def __hash__(self):
        return hash(self.x)

def test_structures():
    for cls in [S, X, Y, Z, W, V]:
        print(cls)
