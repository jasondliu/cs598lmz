import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
print(s.x)
print(s.y)

print(s.__dict__)
print(s.__dict__['x'])
print(s.__dict__['y'])

s.x = 1
s.y = 2
print(s.x)
print(s.y)

print(s.__dict__)
print(s.__dict__['x'])
print(s.__dict__['y'])

s.__dict__['x'] = 3
s.__dict__['y'] = 4
print(s.x)
print(s.y)

print(s.__dict__)
print(s.__dict__['x'])
print(s.__dict__['y'])

s.__dict__['z'] = 5
print(s.__dict__)
print(s.__dict__['z'])

print(s.z)

print(s.__dict__['z'
