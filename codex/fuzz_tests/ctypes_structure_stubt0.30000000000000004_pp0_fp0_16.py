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

print(s.__class__)

print(type(s))

print(type(s) == S)

print(type(s) == ctypes.Structure)

print(type(s) == ctypes.Structure)

print(isinstance(s, ctypes.Structure))

print(isinstance(s, ctypes.Structure))

print(isinstance(s, S))

print(isinstance(s, S))
