import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint8
    y = ctypes.c_uint8
    z = ctypes.c_uint8

s = S(2, 3, 4)
print(s)

# S(x=3, y=3, z=4)
</code>

