import ctypes

class S(ctypes.Structure):
    x = ctypes.c_short
    y = ctypes.c_short
    z = ctypes.c_short
    w = ctypes.c_short

S._fields_ = [
    ("x", ctypes.c_short * 4),
    ("y", ctypes.c_short * 4),
    ("z", ctypes.c_short * 4),
    ("w", ctypes.c_short * 4),
]

s = S()
s.x = [1, 2, 3, 4]
s.y = [5, 6, 7, 8]
s.z = [9, 10, 11, 12]
s.w = [13, 14, 15, 16]

print s.x
print s.y
print s.z
print s.w
</code>
the output:
<code>[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
</code>
instead of the expected:
<code>[1, 2, 3,
