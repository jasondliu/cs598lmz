import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_char_p)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_char_p)]

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.c_char_p)]

class G(ctypes.Structure):
    _fields_ = [('x', ctypes.c_char_p)]

class H(ctypes.Structure):
    _fields_ = [('x', ctypes.c_char_p)]

class I(ctypes.Structure):
    _fields_ = [('x', ctypes.c_char_p)]

class J(ctypes.Structure):
    _fields_ = [('x', ctypes.c_char_p)]

class K(ctypes.Structure):
    _fields_ = [
