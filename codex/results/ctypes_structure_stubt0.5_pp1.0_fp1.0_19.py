import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
print(s.x, s.y)
s.x = 1
s.y = 2
print(s.x, s.y)

s = S(1, 2)
print(s.x, s.y)
s = S(x=1, y=2)
print(s.x, s.y)
s = S(*[1, 2])
print(s.x, s.y)
s = S(**{'x': 1, 'y': 2})
print(s.x, s.y)

s = S(1, 2, 3)
print(s.x, s.y)
s = S(x=1, y=2, z=3)
print(s.x, s.y)
s = S(*[1, 2, 3])
print(s.x, s.y)
s = S(**{'x': 1, 'y': 2, 'z': 3})
print(s.x, s.
