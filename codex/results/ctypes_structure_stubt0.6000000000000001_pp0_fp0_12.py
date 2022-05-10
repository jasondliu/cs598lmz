import ctypes

class S(ctypes.Structure):
    x = ctypes.c_byte
    y = ctypes.c_byte
    z = ctypes.c_short

s = S(1, 2, 3)

print(s.x, s.y, s.z)

s2 = S(1, 2, 3)
s2.x, s2.z = s2.z, s2.x

print(s2.x, s2.y, s2.z)
</code>
Output:
<code>1 2 3
3 2 1
</code>

