import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
print(s.x)
print(s.y)

s.x = 1
s.y = 2

print(s.x)
print(s.y)

print(s)
print(s.x)
print(s.y)

s = S(1, 2)
print(s)
print(s.x)
print(s.y)

s = S(y=2, x=1)
print(s)
print(s.x)
print(s.y)

s = S(x=1)
print(s)
print(s.x)
print(s.y)

s = S(y=2)
print(s)
print(s.x)
print(s.y)

s = S(1)
print(s)
print(s.x)
print(s.y)

s = S(2)
print(s)
print(s.x)
print(s
