import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(42)
    _fields_ = [('x', ctypes.c_int, 2)]

print S().x
</code>

