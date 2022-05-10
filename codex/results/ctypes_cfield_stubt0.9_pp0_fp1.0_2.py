import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(object):
    pass

a1 = A()

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_void_p)]

class B(object):
    def __init__(self):
        self.data = S2()

b1 = B()
b1.data.x = id(a1)
x = b1.data.x
if type(x) is not ctypes.CField:
    raise Exception("Expected ctypes.CField!")
if x._type_ is not ctypes.c_void_p:
    raise Exception("Expected ctypes.c_void_p!")
s = S2((x,))
y = s.x
if type(y) is not ctypes.CField:
    raise Exception("Expected ctypes.CField!")
if y._type_ is not ctypes.c_void_p:
    raise Exception("Expected ctypes.c_void_p!")
if y == 0:
    raise Exception("Expected non
