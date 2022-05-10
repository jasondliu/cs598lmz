import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)                              # True

ctypes.c_int.from_address(ctypes.addressof(s.x))       # True
</code>

