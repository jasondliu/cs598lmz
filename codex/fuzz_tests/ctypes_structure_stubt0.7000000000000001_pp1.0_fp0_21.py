import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ulong(1)
    y = ctypes.c_ulong(2)

print S.x.offset
print S.y.offset
</code>
Output:
<code>0
8
</code>

