import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

def f(x, y, z):
    return x + y + z

f.argtypes = [S, S, S]
f.restype = S

s1 = S(1, 2, 3)
s2 = S(4, 5, 6)
s3 = S(7, 8, 9)

print(f(s1, s2, s3))
</code>

