import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long()
    x = ctypes.c_long()

s = S()
print(ctypes.sizeof(s))
</code>
output:
<code>8
</code>

