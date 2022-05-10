import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long.in_dll(ctypes, 'x')
    _fields_ = [('x', ctypes.c_long), ('y', ctypes.c_long)]

class D(ctypes.Structure):
    x = ctypes.c_long.in_dll(ctypes, 'x')
    _fields_ = [('x', ctypes.c_long)]

S()
D()
</code>

