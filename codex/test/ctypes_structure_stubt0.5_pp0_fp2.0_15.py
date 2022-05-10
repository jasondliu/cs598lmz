import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long()

class A(ctypes.Structure):
    _fields_ = [('s', S)]

class B(ctypes.Structure):
    _fields_ = [('s', S)]

class C(ctypes.Structure):
    _fields_ = [('a', A), ('b', B)]

c = C()
c.a.s.x = 1
c.b.s.x = 2

