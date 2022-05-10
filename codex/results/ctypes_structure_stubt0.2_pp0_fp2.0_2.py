import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
s.x = 1
s.y = 2
s.z = 3

print(s.x)
print(s.y)
print(s.z)

print(s.__dict__)
print(s.__sizeof__())
print(s.__slots__)
print(s.__str__())
print(s.__weakref__)

print(s.x.__class__)
print(s.x.__class__.__name__)
print(s.x.__class__.__module__)
print(s.x.__class__.__bases__)
print(s.x.__class__.__dict__)
print(s.x.__class__.__doc__)
print(s.x.__class__.__mro__)
print(s.x.__class__.__subclasses__())
print(s.x.__class__.__base__
