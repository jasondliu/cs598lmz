import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x)
print(s.y)

print(s.__dict__)

print(s.__dict__['x'])
print(s.__dict__['y'])

print(s.__dict__['x'] == s.x)
print(s.__dict__['y'] == s.y)

print(s.__dict__['x'] is s.x)
print(s.__dict__['y'] is s.y)

print(s.__dict__['x'] is s.__dict__['x'])
print(s.__dict__['y'] is s.__dict__['y'])

print(s.x is s.__dict__['x'])
print(s.y is s.__dict__['y'])

print(s.x is s.y)
