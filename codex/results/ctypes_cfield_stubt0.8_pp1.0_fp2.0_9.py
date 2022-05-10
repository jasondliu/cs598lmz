import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __new__(cls, x):
        self = object.__new__(cls)
        self.x = x
        return self

    def __init__(self, x):
        self.y = x.value * 2

    @property
    def z(self):
        return self.x * 3

def GetCFromS(x):
    return C(x)

def IsCField(x):
    return isinstance(x, ctypes.CField)

class CA(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

class CB(ctypes.Structure):
    _fields_ = [('b', ctypes.c_int)]

def MakeCA(x):
    self = ctypes.pointer(CA())
    self[0].a = x
    return self


# Method resolution order object, with a CField as attribute.
class A(object):
    def __init__(self, x):
        self.a = x

class B
