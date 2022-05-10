import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

class S(ctypes.Structure):
    _fields_ = [('f', FUNTYPE)]

s = S()
s.f = FUNTYPE(lambda x: x*x)
</code>

