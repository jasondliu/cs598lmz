import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint8()

s = S()

s.x = 0
s.x = 1
s.x = 2
s.x = 3
</code>

