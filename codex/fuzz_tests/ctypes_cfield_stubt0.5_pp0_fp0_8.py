import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

ctypes.Structure._fields_ = [('y', ctypes.CField)]

class G(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class H(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class I(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class J(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

ctypes.Structure._fields_ = [('z', ctypes.
