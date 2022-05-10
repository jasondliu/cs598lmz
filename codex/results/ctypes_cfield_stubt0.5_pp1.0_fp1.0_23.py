import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(object):
    def __init__(self, x):
        self.x = x

class B(A):
    def __init__(self, x):
        A.__init__(self, x)
        self.y = x+1

class C(A):
    def __init__(self, x):
        A.__init__(self, x)
        self.z = x+2

class D(B, C):
    def __init__(self, x):
        B.__init__(self, x)
        C.__init__(self, x)

class E(C, B):
    def __init__(self, x):
        C.__init__(self, x)
        B.__init__(self, x)

class F(D, E):
    def __init__(self, x):
        D.__init__(self, x)
        E.__init__(self, x)

class G(F):
    def __init__(self, x):
       
