import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print s.x, s.y
print s.__dict__
</code>
The output is:
<code>1 2
{'x': 1, 'y': 2}
</code>

