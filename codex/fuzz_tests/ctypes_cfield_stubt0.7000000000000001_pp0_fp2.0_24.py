import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A:
    def __init__(self):
        self.b = 1

class B(A):
    def __init__(self):
        A.__init__(self)
        self.c = 2

class C(B):
    def __init__(self):
        B.__init__(self)
        self.d = 3

def f(obj):
    return obj.b

ctypes.CFieldInstance = type(S().x)

class D:
    def __init__(self):
        self.x = 1
    def method(self):
        return self.x

class E(D):
    def __init__(self):
        D.__init__(self)
        self.y = 2
    def method(self):
        return self.y

class F(E):
    def __init__(self):
        E.__init__(self)
        self.z = 3
    def method(self):
        return self.z

class G:
    def __init__(self):
