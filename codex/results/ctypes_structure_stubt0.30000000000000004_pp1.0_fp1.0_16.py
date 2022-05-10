import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)

print(s.x.__class__)
print(s.y.__class__)

print(s.x.__class__.__base__)
print(s.y.__class__.__base__)

print(s.x.__class__.__base__.__base__)
print(s.y.__class__.__base__.__base__)

print(s.x.__class__.__base__.__base__.__base__)
print(s.y.__class__.__base__.__base__.__base__)

print(s.x.__class__.__base__.__base__.__base__.__base__)
print(s.y.__class__.__base__.__base__.__base__.__base__)

print(s.x.__class__.__base
