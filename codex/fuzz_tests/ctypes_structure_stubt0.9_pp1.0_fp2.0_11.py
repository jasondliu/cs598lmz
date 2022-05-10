import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_float()

obj = S()
# obj.x = 5
# print(obj.x)
print(dir(obj))
obj.y = 1.5
print(obj.y)
