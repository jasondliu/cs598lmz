import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)

s = S()
print(s.x)
print(s.y)

s.x = 3
print(s.x)
print(s.y)

s.x = 4
print(s.x)
print(s.y)

s.y = 5
print(s.x)
print(s.y)

s.y = 6
print(s.x)
print(s.y)

s.x = 7
print(s.x)
print(s.y)

s.x = 8
print(s.x)
print(s.y)

s.y = 9
print(s.x)
print(s.y)

s.y = 10
print(s.x)
print(s.y)

s.x = 11
print(s.x)
print(s.y)

s.x = 12
print(s.x)
print(s.y)

s
