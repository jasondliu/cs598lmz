import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char('x')
    y = ctypes.c_char('y')
    _fields_ = [("x", ctypes.c_char),
                ("y", ctypes.c_char)]

s = S()

for field in s._fields_:
    print field[0], getattr(s, field[0])
