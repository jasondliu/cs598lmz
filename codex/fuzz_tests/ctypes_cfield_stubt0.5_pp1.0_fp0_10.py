import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    pass

s = S()
s.x = 7

# setattr(C, 'x', s.x)
# setattr(C, 'x', S.x)
# setattr(C, 'x', ctypes.CField)
setattr(C, 'x', ctypes.c_int)

print(C.x)

c = C()
c.x = 7
print(c.x)
