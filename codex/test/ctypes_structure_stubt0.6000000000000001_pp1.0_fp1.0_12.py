import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)

a = S()
b = S()

print(a.x)
print(b.x)

a.x = ctypes.c_int(3)

print(a.x)
print(b.x)

c = S()
c.x = a.x
a.x = ctypes.c_int(4)

print(a.x)
print(b.x)
print(c.x)
