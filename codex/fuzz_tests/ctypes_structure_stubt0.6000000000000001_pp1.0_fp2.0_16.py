import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()

s = S()
print s.x
s.x = 5
print s.x
</code>
Output:
<code>0
5
</code>

