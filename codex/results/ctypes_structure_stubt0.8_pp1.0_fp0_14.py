import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)

s = S()
s.y = 5
s.x = 6
print s.x
print s.y
</code>
This will print:
<code>6
5
</code>

