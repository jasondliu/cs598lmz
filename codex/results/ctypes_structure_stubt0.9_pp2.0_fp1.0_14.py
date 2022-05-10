import ctypes

class S(ctypes.Structure):
    x = ctypes.int32()
    y = ctypes.int32()
x = S()
x.y = 10
print(x.y)

'''


class PointsDict(ctypes.Structure):
    x = ctypes.Structure._fields_ = [("x", ctypes.c_float),("y", ctypes.c_float)]

for i in PointsDict:
    print(i.__class__)
#x = ctypes.c_float(5.5)
#y = ctypes.c_float(6.6)
#print("x = ",x)
#print("y = ",y)
#print("type of x = ",type(x))
#print("type of y = ",type(y))
#print(ctypes.sizeof(x))
#print(ctypes.sizeof(y))

'''



x = ctypes.c_float()
y = ctypes.c_float()
z = ctypes.c_float()

x.value = 5.5
y.value = 6.6
