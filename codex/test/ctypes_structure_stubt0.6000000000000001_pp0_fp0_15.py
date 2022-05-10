import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char
    y = ctypes.c_char
    z = ctypes.c_char

class V(ctypes.Structure):
    _fields_ = [('s', S), ('c', ctypes.c_char)]

v = V()
v.s.x = 'a'
v.s.y = 'b'
v.s.z = 'c'
