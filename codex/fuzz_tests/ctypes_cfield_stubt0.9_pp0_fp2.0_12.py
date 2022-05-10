import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
cfield = S.x
</code>
However it is strongly recommended not to mess around with the internals of the ctypes machinery.

