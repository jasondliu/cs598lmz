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
print(s._fields_)
print(s._asdict())

print(s._asdict()['x'])
print(s._asdict()['y'])

print(s._asdict()['x'] + s._asdict()['y'])

print(s.x + s.y)

print(s.__dict__['x'])
print(s.__dict__['y'])

print(s.__dict__['x'] + s.__dict__['y'])
