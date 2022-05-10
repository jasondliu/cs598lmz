import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char

class T(ctypes.Structure):
    _fields_ = [("y", ctypes.c_char)]

class U(ctypes.Structure):
    _fields_ = [("z", ctypes.c_char)]

class V(T, U):
    pass

class W(U, T):
    pass

class X(T, S):
    pass

class Y(S, T):
    pass

class Z(S, V):
    pass

class A(V, S):
    pass

class B(S, W):
    pass

class C(W, S):
    pass

