import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S(1, 2, 3)

print(s.x)
print(s.y)
print(s.z)

print(s.__dict__)

print(s.__sizeof__())

print(S.__dict__)

print(S.__sizeof__())

print(s.__class__)

print(s.__class__.__dict__)

print(s.__class__.__sizeof__())

print(s.__class__.__base__)

print(s.__class__.__base__.__dict__)

print(s.__class__.__base__.__sizeof__())

print(s.__class__.__base__.__base__)

print(s.__class__.__base__.__base__.__dict__)

print(s.__class__.__base__.__base__.__sizeof__())
