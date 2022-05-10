import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Union):
    _fields_ = [('y', ctypes.c_int)]

ctypes.CUnion = type(C)

class S2(ctypes.Structure):
    _fields_ = [('a', ctypes.c_ubyte),
                ('b', ctypes.c_ubyte, 4),
                ('c', ctypes.c_ubyte, 4)]

CFieldTest = type(S2.a)

try:
    ctypes.CField = type(S2.b)
except TypeError:
    pass
else:
    raise Exception("expected TypeError")

class S3(ctypes.Structure):
    _fields_ = [('a', ctypes.c_ubyte),
                ('b', ctypes.c_ubyte, 3),
                ('c', ctypes.c_ubyte, 5)]

try:
    ctypes.CField = type(S3.b)
except TypeError:
    pass
else:
    raise Exception("expected TypeError
