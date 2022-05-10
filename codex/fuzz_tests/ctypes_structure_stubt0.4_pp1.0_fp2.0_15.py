import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    def __init__(self):
        self.x = 5

s = S()
print s.x
s.x = 10
print s.x
</code>

