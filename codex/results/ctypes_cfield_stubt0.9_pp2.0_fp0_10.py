import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def flags(value):
    return value

d = {'size': ctypes.sizeof(S),
     'alignment': ctypes.alignment(S),
     'type': S,
     'field_type': ctypes.CField,
     'fi_flags': flags(0),
     'fi_type': ctypes.
