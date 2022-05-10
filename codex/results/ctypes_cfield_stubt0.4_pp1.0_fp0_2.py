import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

assert C().x == 0

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField(ctypes.c_int, 0))]

assert C().x == 0

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField(ctypes.c_int, 1))]

assert C().x == 1

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField(ctypes.c_int, 1, 1))]

assert C().x == 1

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField(ctypes.c_int, 1, 1, 1))]

assert C().x == 1

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField(ctypes.c_int,
