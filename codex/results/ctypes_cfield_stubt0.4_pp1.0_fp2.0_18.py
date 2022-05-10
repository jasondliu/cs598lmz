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

class E(C):
    def __init__(self, x, y):
        super(E, self).__init__(x)
        self.y = y

class F(C):
    def __init__(self, x, y):
        super(F, self).__init__(x)
        self.y = y

class G(C):
    def __init__(self, x, y):
        super(G, self).__init__(x)
        self.y = y

class H(C):
    def __init__(self, x, y):
        super(H, self).__init__(x)
        self.y = y

class I(C):
    def __init__(self, x, y):
        super(I, self
