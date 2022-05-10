import ctypes

class S(ctypes.Structure):
    x = ctypes.POINTER(ctypes.c_int)

s = S()
s.x = ctypes.cast(ctypes.c_int(42), ctypes.POINTER(ctypes.c_int))
s.x[0] = 43
print s.x[0]
</code>

