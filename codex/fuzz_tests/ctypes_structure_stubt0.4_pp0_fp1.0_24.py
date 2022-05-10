import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)

s = S()
s.x = 2
print(s.x)
</code>
Output:
<code>2
</code>

