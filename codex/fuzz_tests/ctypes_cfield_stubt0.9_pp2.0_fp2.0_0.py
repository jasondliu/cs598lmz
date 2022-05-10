import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class P(ctypes.Structure):
    x = ctypes.c_int

for item in [S, P]:
    for field in item._fields_:
        print(type(field[0]))
