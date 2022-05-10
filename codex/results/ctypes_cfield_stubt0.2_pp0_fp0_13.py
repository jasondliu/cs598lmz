import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

C()

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

D()

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

E()

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

F()

class G(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

G()

class H(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

H()

class I(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

I()

class J(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

J()

class K(ctypes
