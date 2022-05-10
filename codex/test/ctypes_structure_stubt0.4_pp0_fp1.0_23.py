import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

class T(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
t = T()

print(s.x, s.y, s.z)
print(t.x, t.y, t.z)

s.x = 1
s.y = 2
s.z = 3

t.x = 4
t.y = 5
t.z = 6

print(s.x, s.y, s.z)
print(t.x, t.y, t.z)
