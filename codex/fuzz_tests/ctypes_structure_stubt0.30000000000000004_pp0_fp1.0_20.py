import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
print(s.x)
print(s.y)
print(s.x.value)
print(s.y.value)

s.x = 1
s.y = 2
print(s.x)
print(s.y)
print(s.x.value)
print(s.y.value)

s.x.value = 3
s.y.value = 4
print(s.x)
print(s.y)
print(s.x.value)
print(s.y.value)

print(s.x == 3)
print(s.y == 4)
print(s.x == s.y)
print(s.x == s.x)
print(s.y == s.y)

print(s.x != 3)
print(s.y != 4)
print(s.x != s.y)
print(s.x != s.x)
print(s.y != s.y)

print
