import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class A(S):
    pass

class B(S):
    pass

class C(A, B):
    pass

class D(B, A):
    pass

