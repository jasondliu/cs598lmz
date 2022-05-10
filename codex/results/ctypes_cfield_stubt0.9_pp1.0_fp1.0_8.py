import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.CField):
    pass

class A(object):
    __slots__ = ['x']
    _fields_ = [('a', ctypes.POINTER(ctypes.c_int))]

class B(A):
    def __init__(self):
        self.x = C()

class C(A):
    pass

def f(b):
    b.x = ctypes.pointer(ctypes.c_int(42))

f(B())
f(C())
