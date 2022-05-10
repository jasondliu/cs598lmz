import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int64(1)
    y = ctypes.c_int64(2)
    z = ctypes.c_int64(3)

s = S()
a = ctypes.addressof(s)
print(ctypes.sizeof(s))
print(a)
print(a+1)
print(a+2)
print(a+3)
print(a+4)
print(a+5)
print(a+6)
print(a+7)
