import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
s.x = 1
s.y = 2
s.z = 3

s2 = S.from_buffer(s)
s2.x = 4
s2.y = 5
s2.z = 6

print(s.x, s.y, s.z)
print(s2.x, s2.y, s2.z)

# 1 2 3
# 4 5 6
</code>

