import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.c_int):
    def __init__(self):
        ctypes.c_int.__init__(self, 42)

class Y(ctypes.c_int):
    def __init__(self):
        ctypes.c_int.__init__(self, 42)
    def __new__(cls):
        return ctypes.c_int.__new__(cls, 42)

class Z(ctypes.c_int):
    def __init__(self):
        ctypes.c_int.__init__(self, 42)
    def __new__(cls):
        return ctypes.c_int.__new__(cls)

class A(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class B(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __init__(self):
        self.x = 42

class C(ctypes.Structure):
   
