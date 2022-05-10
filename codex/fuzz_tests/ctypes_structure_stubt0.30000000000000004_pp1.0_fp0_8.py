import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
    ]

class C(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.c_int),
        ('s', S),
    ]

c = C()
print c.a, c.b, c.s.x, c.s.y
c.a = 1
c.b = 2
c.s.x = 3
c.s.y = 4
print c.a, c.b, c.s.x, c.s.y
</code>
Output:
<code>0 0 0 0
1 2 3 4
</code>

