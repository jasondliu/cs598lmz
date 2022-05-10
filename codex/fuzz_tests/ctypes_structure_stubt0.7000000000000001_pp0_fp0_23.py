import ctypes

class S(ctypes.Structure):
    x = (ctypes.c_byte * 3)(1,2,3)
s = S()
print(s.x[0])
s.x[0] = 4
print(s.x[0])
</code>
This gives the output:
<code>1
4
</code>

