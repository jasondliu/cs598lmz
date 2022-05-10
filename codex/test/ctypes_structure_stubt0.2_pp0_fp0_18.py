import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)
print(s.__dict__)

s.__dict__['x'] = 3
print(s.x, s.y)
print(s.__dict__)

s.__dict__['z'] = 4
print(s.x, s.y)
print(s.__dict__)

s.__dict__['x'] = 5
print(s.x, s.y)
print(s.__dict__)

s.__dict__['x'] = 6
print(s.x, s.y)
print(s.__dict__)

s.__dict__['x'] = 7
print(s.x, s.y)
print(s.__dict__)

s.__dict__['x'] = 8
print(s.x, s.y)
print(s.__dict__)

