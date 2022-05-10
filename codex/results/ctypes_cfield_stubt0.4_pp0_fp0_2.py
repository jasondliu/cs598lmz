import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

S._fields_[0] = ('x', ctypes.c_int)

s = S()
print(s.x)

c = C()
print(c.x)
