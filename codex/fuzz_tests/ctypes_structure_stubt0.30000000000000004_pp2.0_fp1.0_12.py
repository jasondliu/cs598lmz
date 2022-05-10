import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)

s2 = S(2, 3)
print(s2.x, s2.y)

s3 = S(x=4, y=5)
print(s3.x, s3.y)

s4 = S(y=6, x=7)
print(s4.x, s4.y)

s5 = S(1, y=2)
print(s5.x, s5.y)

try:
    s6 = S(1, 2, 3)
except TypeError:
    print("TypeError")

try:
    s7 = S(1, y=2, z=3)
except TypeError:
    print("TypeError")

try:
    s8 = S(1, 2, x=3)
except TypeError:
    print("TypeError")

try:
    s9 = S
