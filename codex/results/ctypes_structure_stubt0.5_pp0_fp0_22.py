import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

print(ctypes.sizeof(S))

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)
</code>

