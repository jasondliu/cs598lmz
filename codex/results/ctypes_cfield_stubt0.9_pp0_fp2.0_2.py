import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class R(ctypes.Structure):
    _fields_ = [('fp', ctypes.CField)]

print R.fp
print R.fp.__doc__
print R.fp.offset
print R.fp.size
