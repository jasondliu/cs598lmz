import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

s = S()
print type(s.x)
print s.x.__class__
sys.stdout.flush()
