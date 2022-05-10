import ctypes

class S(ctypes.Structure):
    x = ctypes.c_short
    y = ctypes.c_long
S._fields_ = [('x', ctypes.c_short), ('y', ctypes.c_long)]
a = S()
a.x

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_short), ('y', ctypes.c_long)]
    x = y = ctypes.c_short(1)
a = S()
a.x

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_short), ('y', ctypes.c_long)]
    x = y = ctypes.c_short(1)
a = S()
a.x

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_short), ('y', ctypes.c_long)]
    x = y = ctypes.c_short(1)
a = S()
a.x

