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

# int *p = &s.x;
p = ctypes.pointer(s.x)
print(p.contents)
print(p.contents.value)

# int *p = &s.y;
p = ctypes.pointer(s.y)
print(p.contents)
print(p.contents.value)

# int *p = &s.z;
p = ctypes.pointer(s.z)
print(p.contents)
print(p.contents.value)
