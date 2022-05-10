import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

C.y = ctypes.CField

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.CField)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.CField)]

E.y = ctypes.CField

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.CField)]

F.y = ctypes.CField
F.z = ctypes.c_int

class G(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.CField),
                ('z', ctypes.c_int)]

class H(ctypes.Structure):
    _fields
