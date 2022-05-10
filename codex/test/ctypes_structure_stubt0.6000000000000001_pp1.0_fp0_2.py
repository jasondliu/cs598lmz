import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [('x', x)]

S()
S(x=1)
S(*[1])
S(**{'x': 1})
S(1)
