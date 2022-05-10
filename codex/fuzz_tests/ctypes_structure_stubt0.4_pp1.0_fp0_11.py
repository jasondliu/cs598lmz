import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint32
    y = ctypes.c_uint32

def f(s):
    return s.x + s.y

s = S()
s.x = 1
s.y = 2
print(f(s))
</code>

