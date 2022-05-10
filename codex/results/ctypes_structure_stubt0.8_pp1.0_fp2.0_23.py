import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long
    _fields_ = [("[" + str(i) + "]", ctypes.c_long) for i in range(1024)]

s = S()
s.arr_0 = 1
s.arr_1 = 2
print s.x
