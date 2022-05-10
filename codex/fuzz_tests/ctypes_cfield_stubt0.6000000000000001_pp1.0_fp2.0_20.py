import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.Structure):
    _fields_ = [('y', ctypes.CField)]

class Y(ctypes.Structure):
    _fields_ = [('z', ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [('y', Y)]

X()
Y()
Z()
