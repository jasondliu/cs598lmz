import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    _fields_ = [
            ("y", ctypes.c_int),
            ("z", ctypes.c_int),
            ]

s = S()

print(s.x)
print(s.y)
print(s.z)
</code>
The output is:
<code>0
0
0
</code>

