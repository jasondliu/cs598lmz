import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float(1.0)

s = S()
s.x = 2.0
print s.x
</code>
The output is <code>2.0</code>.

