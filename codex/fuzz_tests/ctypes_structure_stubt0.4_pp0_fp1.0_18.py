import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
s.x = 1
s.y = 2

print s.x
print s.y
</code>
The output is:
<code>1
2
</code>

