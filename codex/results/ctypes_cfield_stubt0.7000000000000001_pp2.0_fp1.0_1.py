import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class F(ctypes.Structure):
    _fields_ = [('name', ctypes.c_char), ('f', ctypes.CField)]

s = S()
s.x = 4
f = F(b'x', s.x)
print(f.name)
print(f.f)
