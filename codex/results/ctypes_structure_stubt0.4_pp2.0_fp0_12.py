import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_int)
    ]

s = S(1, 2)
print(s.x, s.y)
print(s[0], s[1])
print(s.__getitem__(0), s.__getitem__(1))
print(s[0:2])
print(s.__getitem__(slice(0, 2)))
</code>
Output:
<code>1 2
1 2
1 2
(1, 2)
(1, 2)
</code>

