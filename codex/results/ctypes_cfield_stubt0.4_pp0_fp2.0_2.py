import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.CField):
    pass

class Y(ctypes.CField):
    _fields_ = [('y', ctypes.c_int)]

class Z(ctypes.CField):
    _fields_ = [('z', ctypes.c_int)]

class W(ctypes.CField):
    _fields_ = [('w', ctypes.c_int)]

class A(ctypes.Structure):
    _fields_ = [('a', X)]

class B(ctypes.Structure):
    _fields_ = [('a', Y)]

class C(ctypes.Structure):
    _fields_ = [('a', Z)]

class D(ctypes.Structure):
    _fields_ = [('a', W)]

class E(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

class F(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

class G(ctypes.St
