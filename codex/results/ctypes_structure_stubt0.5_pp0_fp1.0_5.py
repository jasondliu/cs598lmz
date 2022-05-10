import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int16
    y = ctypes.c_int16
    z = ctypes.c_int16
    w = ctypes.c_int16

s = S()
s.x = 1
s.y = 2
s.z = 3
s.w = 4

print(s.x)
print(s.y)
print(s.z)
print(s.w)
</code>
Output:
<code>1
2
3
4
</code>

