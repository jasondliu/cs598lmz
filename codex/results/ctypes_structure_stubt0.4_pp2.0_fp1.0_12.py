import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()

print(s.x)
print(s.y)
print(s.z)

s.x = 1
s.y = 2
s.z = 3

print(s.x)
print(s.y)
print(s.z)

t = S()

print(t.x)
print(t.y)
print(t.z)

t.x = 4
t.y = 5
t.z = 6

print(t.x)
print(t.y)
print(t.z)

print(s.x)
print(s.y)
print(s.z)

s.x = 7
s.y = 8
s.z = 9

print(s.x)
print(s.y)
print(s.z)

print(t.x)
print(t.y)
print(t.z)
