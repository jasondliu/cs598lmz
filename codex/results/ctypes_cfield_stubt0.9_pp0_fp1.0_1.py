import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

print 'type(S.x) =>', type(S.x)
print S.__name__
print ctypes.CField.__name__
