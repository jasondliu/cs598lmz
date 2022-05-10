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

s.__dict__['x'] = 100

print(s.x)
print(s.y)
print(s.z)

print(s.__dict__)

s.x = 200

print(s.x)
print(s.y)
print(s.z)

print(s.__dict__)

s.__dict__['x'] = 300

print(s.x)
print(s.y)
print(s.z)

print(s.__dict__)

s.x = 400

print(s.x)
print(s.y)
print(s.z)

print(s.__dict__)
