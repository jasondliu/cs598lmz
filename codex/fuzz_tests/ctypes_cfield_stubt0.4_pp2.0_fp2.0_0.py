import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, x):
        self.x = x

class D(C):
    def __init__(self, x):
        C.__init__(self, x)

class E(C):
    def __init__(self, x):
        C.__init__(self, x)

class F(D, E):
    def __init__(self, x):
        D.__init__(self, x)
        E.__init__(self, x)

class G(D, E):
    def __init__(self, x):
        D.__init__(self, x)
        E.__init__(self, x)
        self.x = x

class H(D, E):
    def __init__(self, x):
        D.__init__(self, x)
        E.__init__(self, x)
        self.x = x
    def __getattribute__(self, name):
        return object.__getattribute__(self,
