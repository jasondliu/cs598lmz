import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float()
    y = ctypes.c_float()


S._fields_ = [('x', ctypes.c_float), ('y', ctypes.c_float)]

x = S.x.offset
y = S.y.offset

s = S()
s.x = 1.2
s.y = 3.4

