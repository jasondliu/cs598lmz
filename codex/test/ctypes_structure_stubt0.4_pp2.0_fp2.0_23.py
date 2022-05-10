import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

def f(x, y):
    return x + y

s = S()
s.x = 1
s.y = 2

print(f(s.x, s.y))
print(f(s.x, s.y))
print(f(s.x, s.y))
print(f(s.x, s.y))
print(f(s.x, s.y))
print(f(s.x, s.y))
print(f(s.x, s.y))
print(f(s.x, s.y))
print(f(s.x, s.y))
print(f(s.x, s.y))
print(f(s.x, s.y))
print(f(s.x, s.y))
print(f(s.x, s.y))
print(f(s.x, s.y))
print(f(s.x, s.y))
