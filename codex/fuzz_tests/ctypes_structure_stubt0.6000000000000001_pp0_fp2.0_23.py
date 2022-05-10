import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint64
    y = ctypes.c_uint64

s = S(1, 2)
print(s.x, s.y)

s = S(x=1, y=2)
print(s.x, s.y)

s = S(y=2, x=1)
print(s.x, s.y)

s = S(1)
print(s.x, s.y)

s = S(1, y=2)
print(s.x, s.y)

s = S(x=1)
print(s.x, s.y)

try:
    s = S(1, 2, 3)
except TypeError as e:
    print(e)

try:
    s = S(1, 2, y=3)
except TypeError as e:
    print(e)

try:
    s = S(1, x=2, y=3)
except TypeError as e:
    print(e)

try:
    s = S(
