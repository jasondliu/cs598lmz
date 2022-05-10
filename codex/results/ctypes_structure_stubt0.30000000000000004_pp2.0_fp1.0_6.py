import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)

# ctypes.Structure.__dict__['x'].__set__(s, 3)
setattr(s, 'x', 3)

print(s.x, s.y)
</code>
Output:
<code>1 2
3 2
</code>

