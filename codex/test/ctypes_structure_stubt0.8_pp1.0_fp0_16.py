import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class A(S):
    _fields_ = [('y', ctypes.c_int)]

class B(S):
    _fields_ = [('z', ctypes.c_int)]

class C(A, B):
    pass

