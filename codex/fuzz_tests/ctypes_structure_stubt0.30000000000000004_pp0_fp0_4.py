import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int
    def __init__(self):
        self.x = 1
        self.y = 2
        self.z = 3

s = S()
print s.x, s.y, s.z

s.x = 10
s.y = 20
s.z = 30
print s.x, s.y, s.z
</code>

