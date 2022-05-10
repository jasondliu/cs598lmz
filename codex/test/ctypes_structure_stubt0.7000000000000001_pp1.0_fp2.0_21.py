import ctypes

class S(ctypes.Structure):
    x = ctypes.c_short
    y = ctypes.c_short
    _fields_ = [('x', ctypes.c_short), ('y', ctypes.c_short)]

class U(ctypes.Union):
    x = ctypes.c_short
    y = ctypes.c_short
    _fields_ = [('x', ctypes.c_short), ('y', ctypes.c_short)]

class T(ctypes.Structure):
    s = S()
    u = U()
    _fields_ = [('s', S), ('u', U)]

print(ctypes.sizeof(S))
print(ctypes.sizeof(T))
print(ctypes.sizeof(ctypes.c_short))
