import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

C()

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField * 1)]

C()

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField * 2)]

C()
