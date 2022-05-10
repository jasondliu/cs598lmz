import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

a = S()
a.x = 1
a.y = 2

b = S()
b.x = 3
b.y = 4

print(a.x, a.y)
print(b.x, b.y)

a = b

print(a.x, a.y)
print(b.x, b.y)

a.x = 5
a.y = 6

print(a.x, a.y)
print(b.x, b.y)
