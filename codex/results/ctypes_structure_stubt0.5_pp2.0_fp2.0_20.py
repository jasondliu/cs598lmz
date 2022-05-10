import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint32()
    y = ctypes.c_uint32()

s = S()
s.x = 1
s.y = 1

print s.x, s.y
</code>
prints
<code>1 1
</code>

