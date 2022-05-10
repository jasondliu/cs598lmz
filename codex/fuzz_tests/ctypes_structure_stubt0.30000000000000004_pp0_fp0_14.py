import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print s.x, s.y
print s.x.value, s.y.value
</code>
Output:
<code>1 2
1 2
</code>

