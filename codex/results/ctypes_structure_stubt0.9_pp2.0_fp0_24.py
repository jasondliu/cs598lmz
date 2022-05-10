import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ushort * 2

obj = S()
obj.x[1] = 3
</code>

