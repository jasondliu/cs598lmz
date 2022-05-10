import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S(1, 2, 3)
print(s.x, s.y, s.z)

s.x = 4
print(s.x, s.y, s.z)

s.x = 5
s.y = 6
s.z = 7
print(s.x, s.y, s.z)

t = S(8, 9, 10)
print(t.x, t.y, t.z)

t.x = 11
print(t.x, t.y, t.z)

t.x = 12
t.y = 13
t.z = 14
print(t.x, t.y, t.z)

print(s.x, s.y, s.z)

print(type(s))
print(type(S))

print(isinstance(s, S))
print(isinstance(S, type))

print(isinstance(s, ctypes
