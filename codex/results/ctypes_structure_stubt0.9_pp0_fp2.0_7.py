import ctypes

class S(ctypes.Structure):
    x = None
    pass

ctypes.Structure._fields_ = [('x', ctypes.c_uint),
                             ('y', ctypes.c_uint)]

print S.x
print S().x
