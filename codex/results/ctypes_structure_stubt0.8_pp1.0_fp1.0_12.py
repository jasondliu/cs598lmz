import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    def __init__(self, x):
        self.x = x

s = S(1)
print(s.x)
#1
print(s.__dict__)
#{}
</code>

