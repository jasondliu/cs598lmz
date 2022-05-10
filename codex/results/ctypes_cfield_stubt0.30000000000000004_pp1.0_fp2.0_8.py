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
        super(E, self).__init__(x)

class F(C):
    def __init__(self, x):
        super().__init__(x)

class G(C):
    def __init__(self, x):
        super(C, self).__init__(x)

class H(C):
    def __init__(self, x):
        super(__class__, self).__init__(x)

class I(C):
    def __init__(self, x):
        super(type(self), self).__init__(x)

class J(C):
    def __init__(self, x):
        super(C, type(self)).__init__(x)

class K(C
