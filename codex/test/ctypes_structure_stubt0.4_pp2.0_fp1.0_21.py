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

print(s.__dict__)
print(s.__dict__.keys())
print(s.__dict__.values())

s.__dict__['x'] = 3
print(s.x)

s.__dict__['z'] = 4
print(s.z)

print(s.__dict__)
print(s.__dict__.keys())
print(s.__dict__.values())

print(dir(s))

print(s.__doc__)
print(s.__module__)
print(s.__class__)

print(s.__dict__)
print(s.__dict__.keys())
print(s.__dict__.values())

print(dir(s))
