import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
print(s.x, s.y, s.z)
s.x = 1
s.y = 2
s.z = 3
print(s.x, s.y, s.z)

print(s.__dict__)
print(s.__dict__.keys())
print(s.__dict__.values())
print(s.__dict__.items())

print(s.__slots__)
print(s.__weakref__)
print(s.__doc__)
print(s.__class__)
print(s.__module__)
print(s.__hash__)
print(s.__str__)
print(s.__repr__)
print(s.__format__)
print(s.__sizeof__)
print(s.__dir__)
print(s.__reduce__)
print(s.__reduce_ex__)
print(s.__
