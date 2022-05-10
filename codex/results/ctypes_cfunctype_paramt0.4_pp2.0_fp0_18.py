import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    return a + b

# CMPFUNC = FUNTYPE(func)
# print(CMPFUNC(1, 2))

# 创建一个结构体
class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

point = Point()
point.x = 1
point.y = 2
print(point.x, point.y)

# 创建一个类
class Point2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

point2 = Point2()
point2.x = 1
point2.y = 2
print(point
