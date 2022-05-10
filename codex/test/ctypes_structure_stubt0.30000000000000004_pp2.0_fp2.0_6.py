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

a.x = b.x
a.y = b.y

print(a.x, a.y)
print(b.x, b.y)

b.x = 5
b.y = 6

print(a.x, a.y)
print(b.x, b.y)
