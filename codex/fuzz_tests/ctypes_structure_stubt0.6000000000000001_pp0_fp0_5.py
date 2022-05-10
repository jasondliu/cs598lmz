import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    array = ctypes.c_int * 4

s = S(1, [2, 3, 4, 5])
print(s.x, s.array[0], s.array[1], s.array[2], s.array[3])
# 1 2 3 4 5
</code>

