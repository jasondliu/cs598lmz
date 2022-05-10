import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(object):
    def __init__(self):
        self.x = ctypes.c_int()
        self.y = ctypes.c_int()

class B(object):
    def __init__(self):
        self.p = ctypes.pointer(ctypes.c_int())
        self.y = ctypes.c_int()

class C(object):
    def __init__(self):
        self.x = ctypes.c_int()
        self.p = ctypes.pointer(ctypes.c_int())

class D(object):
    def __init__(self):
        self.x = ctypes.c_int()
        self.a = A()

class E(object):
    def __init__(self):
        self.a = A()
        self.b = B()

class F(object):
    def __init__(self):
        self.b = B()
        self.c = C()

class G(object):
    def __init__(self):
       
