import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(object):
    def __init__(self):
        pass

S2 = ctypes.Structure
S2._fields_ = [('x', A)]

class B(object):
    def __init__(self):
        pass

A.subclass = B

class C(object):
    def __init__(self):
        pass

B.subclass = C

s = S()
s.x = 42
print s.x

s2 = S2()
s2.x = A()
print s2.x

print s2.x.subclass()
