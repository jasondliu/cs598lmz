import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

S.x.__class__ is ctypes.CField

CField = ctypes.CField

class S(ctypes.Structure):
    _fields_ = [('x', CField)]

type(S.x) is CField

CField = ctypes.CField

class S(ctypes.Structure):
    _fields_ = [('x', CField(ctypes.c_int))]

type(S.x) is CField

CField = ctypes.CField

class S(ctypes.Structure):
    _fields_ = [('x', CField(ctypes.c_int, 0))]

type(S.x) is CField

CField = ctypes.CField

class S(ctypes.Structure):
    _fields_ = [('x', CField(ctypes.c_int, 0, 'x'))]

type(S.x) is CField

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.CField(ct
