import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

s = S()
print(type(s.x))
print(s.x)
setattr(s, 'x', 100)
print(s.x)
setattr(s, 'x', ctypes.c_int(2))
print(s.x)
setattr(s, 'x', ctypes.c_int(3))
print(s.x)

# ctypes.CField
# 0
# 100
# 2
# 3
