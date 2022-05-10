import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S2(ctypes.Structure):
    _fields_ = [('f', S.x.__class__)]

class S3(ctypes.Structure):
    _fields_ = [('f', ctypes.CField)]

print S2().f
print S3().f
