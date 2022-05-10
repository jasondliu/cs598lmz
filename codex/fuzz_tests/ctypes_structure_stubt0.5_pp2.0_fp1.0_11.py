import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(0)
    y = ctypes.c_int(0)

s = S()
s.x = 1
s.y = 2
print s.x, s.y
</code>
This is the output:
<code>1 2
</code>

