import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 5
s.y = 3

print(s.x)
print(s.y)
print(s.x + s.y)

print("")

s1 = S(x = 5, y = 3)
print(s1.x)
print(s1.y)
print(s1.x + s1.y)
