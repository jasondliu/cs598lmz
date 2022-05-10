import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long()
    y = ctypes.c_long()

s = S()
s.x = 1
s.y = 2

print(s.x)
print(s.y)

print(s.__class__)
print(s.__class__.__bases__)
print(s.__class__.__bases__[0].__bases__)

print(s.__class__.__bases__[0].__bases__[0].__bases__)

print(s.__class__.__bases__[0].__bases__[0].__bases__[0].__bases__)

