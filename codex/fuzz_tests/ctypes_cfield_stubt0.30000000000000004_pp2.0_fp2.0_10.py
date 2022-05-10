import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, x):
        self.x = x

class D(C):
    def __init__(self, x, y):
        C.__init__(self, x)
        self.y = y

class E(D):
    def __init__(self, x, y, z):
        D.__init__(self, x, y)
        self.z = z

class F(E):
    def __init__(self, x, y, z, w):
        E.__init__(self, x, y, z)
        self.w = w

class G(F):
    def __init__(self, x, y, z, w, u):
        F.__init__(self, x, y, z, w)
        self.u = u

class H(G):
    def __init__(self, x, y, z, w, u, v):
        G.__init__(self, x, y, z, w, u)
       
