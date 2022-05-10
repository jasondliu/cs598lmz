import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
s.x = 1
s.y = 2
s.z = 3

print(s.x, s.y, s.z)
print(s.__dict__)
print(s.__class__)
print(s.__class__.__dict__)
print(s.__class__.__bases__)
print(s.__class__.__bases__[0].__dict__)
print(s.__class__.__bases__[0].__bases__)
print(s.__class__.__bases__[0].__bases__[0].__dict__)
print(s.__class__.__bases__[0].__bases__[0].__bases__)
print(s.__class__.__bases__[0].__bases__[0].__bases__[0].__dict__)
print(s.__class__.__bases__[
