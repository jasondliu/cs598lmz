import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class C(ctypes.Structure):
    _fields_ = [("s", S),
                ("a", ctypes.c_int)]
    def __init__(self, x, y, z, a):
        self.s = S(x, y, z)
        self.a = a

c = C(1, 2, 3, 4)
print c.s.x, c.s.y, c.s.z, c.a
</code>
The output is <code>1 2 3 4</code>.

