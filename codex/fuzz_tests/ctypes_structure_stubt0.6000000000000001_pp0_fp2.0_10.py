import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_double

s = S()
a = ctypes.byref(s)
a.contents.x = 42
a.contents.y = 3.14

print s.x, s.y
print a.contents.x, a.contents.y
</code>

