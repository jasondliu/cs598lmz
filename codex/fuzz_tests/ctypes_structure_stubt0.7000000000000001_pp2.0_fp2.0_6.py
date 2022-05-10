import ctypes

class S(ctypes.Structure):
    x = 2
    y = 3
    _fields_ = [
        ('x', ctypes.c_byte),
        ('y', ctypes.c_byte),
        ('z', ctypes.c_byte),
        ('w', ctypes.c_byte),
    ]

s = S()
print repr(s)
assert s.x == 2
assert s.y == 3
assert (s.z, s.w) == (0, 0)
</code>
This produces the output
<code>&lt;ctypes.Structure object at 0x7f53a841e5d0&gt;
</code>

