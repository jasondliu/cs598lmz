import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong()
    y = ctypes.c_int()
    z = ctypes.c_int()

class T(ctypes.Structure):
    x = ctypes.c_longlong()
    y = ctypes.c_int()
    z = ctypes.c_int()

s = S()
s.x = 4819
s.y = 42
s.z = 13

t = T()
t.x = 4819
t.y = 42
t.z = 13

print(s)
print(t)
print(id(s))
print(id(t))
print(id(s.x))
print(id(t.x))
