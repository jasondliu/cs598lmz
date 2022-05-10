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
print(s.__dict__.keys())
print(s.__dict__.values())

print(s.__dict__['x'])
print(s.__dict__['y'])
print(s.__dict__['z'])

s.__dict__['x'] = 10
s.__dict__['y'] = 20
s.__dict__['z'] = 30

print(s.x)
print(s.y)
print(s.z)

print(s.__dict__)
print(s.__dict__.keys())
print(s.__dict__.values())

print(s.__dict__['x'])
print(s.__dict__['y'])

