import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int16()
    y = ctypes.c_int16()
    z = ctypes.c_int16()
    w = ctypes.c_int16()

obj = S()
obj.x = 1
obj.y = 2
obj.w = 0
print(obj.z is None)
