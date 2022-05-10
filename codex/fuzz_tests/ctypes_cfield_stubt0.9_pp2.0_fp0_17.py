import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

print ctypes.CField
if isinstance(S, ctypes.CField):
    print "1"
else:
    print "2"
