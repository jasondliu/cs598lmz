import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double(1.0)
    y = ctypes.c_double()
    z = ctypes.c_double(3.0)

s = S()

s.y = 2.0

s.x = 4.0
s.z = 5.0

assert s.x == 4.0
assert s.y == 2.0
assert s.z == 5.0

print(s.x)
print(s.y)
print(s.z)
</code>

