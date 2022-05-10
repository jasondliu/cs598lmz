import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()
    z = ctypes.c_int()
S()
print(S().x)
print(S().y)
print(S().z)

s = S()
s.x = 1
s.y = 2
s.z = 3
print(s.x)
print(s.y)
print(s.z)

class T(ctypes.Structure):
    x = ctypes.c_int()
    _fields_ = [("y", ctypes.c_int), ("z", ctypes.c_int)]
T()
print(T().x)
print(T().y)
print(T().z)

t = T()
t.x = 1
t.y = 2
t.z = 3
print(t.x)
print(t.y)
print(t.z)

