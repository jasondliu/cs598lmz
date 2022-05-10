import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class Sp(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

s = S()
print s.x
s.x = 3
print s.x

s = Sp()
print s.x
s.x = 3
print s.x

s = S()
sp = Sp()
s.x = 3
s.y = 4
sp.x = 5
sp.y = 6
print s.x, s.y
print sp.x, sp.y

print ctypes.sizeof(S)
print ctypes.sizeof(Sp)
