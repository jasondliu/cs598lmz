import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
print(s.x)
print(s.y)
print(s.z)
</code>
Output:
<code>0
0
0
</code>

