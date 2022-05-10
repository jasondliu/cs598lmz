import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
    ]

s = S(1, 2)
print(s.x)
print(s.y)
print(s.x == s.y)
</code>
The output is:
<code>1
2
False
</code>

