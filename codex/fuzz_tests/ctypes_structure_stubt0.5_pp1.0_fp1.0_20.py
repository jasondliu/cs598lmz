import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    def __init__(self):
        self.x = 0
        self.y = 0

def f(s):
    s.x = s.x + 1
    s.y = s.y + 1

s = S()
f(s)
print s.x
print s.y
