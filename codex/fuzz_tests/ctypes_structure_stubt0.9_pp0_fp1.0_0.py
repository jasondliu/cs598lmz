import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int16()
    y = ctypes.c_float()
    z = ctypes.c_double()

data1 = S()
data2 = S()

data1.x = 5
data1.y = 5.0
data1.z = 5.0

data2.x = 10
data2.y = 10.5
data2.z = 10.5

print(data1.x, data1.y, data1.z)
print(data2.x, data2.y, data2.z)
