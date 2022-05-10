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

s.x = 3
s.y = 4

print(s.x)
print(s.y)

print(s)

print(s.x)
print(s.y)

s.x = 5
s.y = 6

print(s.x)
print(s.y)

print(s)

print(s.x)
print(s.y)

s.x = 7
s.y = 8

print(s.x)
print(s.y)

print(s)

print(s.x)
print(s.y)

s.x = 9
s.y = 10

print(s.x)

