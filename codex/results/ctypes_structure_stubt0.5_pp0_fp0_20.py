import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

def f():
    s = S()
    s.x = 4
    s.y = 5
    return s

s = f()
print(s.x)
print(s.y)
</code>

