import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
print s.x
print s.y
</code>
This prints:
<code>0
0
</code>

