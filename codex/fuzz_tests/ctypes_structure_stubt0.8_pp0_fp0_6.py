import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
a = S(1, 2)
b = S()
b.x = 1
b.y = 2
print(a == b)
</code>
The result is <code>False</code>.

