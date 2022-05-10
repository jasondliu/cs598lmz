import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long()

class T(ctypes.Structure):
    _fields_ = [("s", S)]

s = S()
t = T()

print t.s.x
t.s = s
print t.s.x
t.s.x = 42
print t.s.x
print s.x
