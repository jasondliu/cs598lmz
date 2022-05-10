import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float
    y = ctypes.c_char

a = S(x=1, y='a')
print(a.x, a.y)
</code>
So it looks like
<code>class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
</code>
is fine, then.

