import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(ctypes.c_char_p):
    pass

class B(ctypes.c_char_p):
    pass

class C(ctypes.c_char_p):
    pass

class D(ctypes.c_char_p):
    pass

class E(ctypes.c_char_p):
    pass

class F(ctypes.c_char_p):
    pass

class G(ctypes.c_char_p):
    pass

class H(ctypes.c_char_p):
    pass

class I(ctypes.c_char_p):
    pass

class J(ctypes.c_char_p):
    pass

class K(ctypes.c_char_p):
    pass

class L(ctypes.c_char_p):
    pass

class M(ctypes.c_char_p):
    pass

class N(ctypes.c_char_p):
    pass

class O(ctypes.c_char_p):
    pass
