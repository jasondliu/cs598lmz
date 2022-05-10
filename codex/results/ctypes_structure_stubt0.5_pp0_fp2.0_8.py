import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1

print s.x
print s.y
print s.__dict__
</code>
Output:
<code>1
0
{'y': 0, 'x': 1}
</code>

