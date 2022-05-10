import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long(3)
    _fields_ = [('x', ctypes.c_long), ('y', ctypes.c_long)]

