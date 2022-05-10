import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
S_p = ctypes.POINTER(S)
s = S()
s.x = 42
s_p = S_p(s)
s_p.x = 42

class A(ctypes.Structure):
    _fields_ = [
        ('s', S_p)
    ]
a = A()
a.s = s_p
a.s.contents.x = 42
