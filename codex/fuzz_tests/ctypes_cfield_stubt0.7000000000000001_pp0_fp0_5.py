import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(ctypes._CData):
    _type_ = "A"
    __slots__ = ['_b_base_']
    _fields_ = [('a', ctypes.c_int)]
    def __init__(self):
        self.a = 1

class B(A):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int)]
    _anonymous_ = ['_b_base_']
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3

class C(A):
    _fields_ = [('c', ctypes.c_int)]
    def __init__(self):
        A.__init__(self)
        self.a = 4
        self.c = 5

class D(B, C):
    _fields_ = [('d', ctypes.c_int), ('_b_base_', A)]
    def __init__(self):
        B.__init
