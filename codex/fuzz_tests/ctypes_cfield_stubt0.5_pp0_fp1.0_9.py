import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.Union):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

ctypes.CUnion = type(X)

class Y(ctypes.Union):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

class Z(Y):
    _anonymous_ = ("y",)

ctypes.CUnion = type(Y)
ctypes.CUnion = type(Z)

class X(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

ctypes.CStructure = type(X)

class Y(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

class Z(Y):
    _anonymous_ = ("y",)

ctypes.CStructure = type(Y)
ctypes.CStructure =
