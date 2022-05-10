import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CFieldType = type(S.x.__class__)

class C(ctypes.Structure):
    pass

C._fields_ = [('x', ctypes.c_int)]

class D(ctypes.Structure):
    pass

D._fields_ = [('x', ctypes.c_int)]

class E(ctypes.Structure):
    pass

E._fields_ = [('x', ctypes.c_int)]

class F(ctypes.Structure):
    pass

F._fields_ = [('x', ctypes.c_int)]

class G(ctypes.Structure):
    pass

G._fields_ = [('x', ctypes.c_int)]

class H(ctypes.Structure):
    pass

H._fields_ = [('x', ctypes.c_int)]

class I(ctypes.Structure):
    pass

I._fields_ = [('x', ctypes.c_int)]

class J(ctypes.Structure):
   
