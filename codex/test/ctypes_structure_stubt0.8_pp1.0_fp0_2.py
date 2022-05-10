import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double
    z = ctypes.c_double

arr = (S*4)()

for idx, v in enumerate(arr):
    v.x = idx + 0.1
    v.y = idx + 0.2
    v.z = idx + 0.3

