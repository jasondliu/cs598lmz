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

s.__dict__['x'] = 100
s.__dict__['y'] = 200

print(s.x)
print(s.y)

print(s.__dict__)

print(s.__dict__['x'])
print(s.__dict__['y'])
