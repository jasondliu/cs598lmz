import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def to_c_field(value):
    return ctypes.CField(int(value))
</code>

