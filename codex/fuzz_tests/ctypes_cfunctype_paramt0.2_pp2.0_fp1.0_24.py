import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(x):
    return x + 1

f = FUNTYPE(func)
print(f(1))

# 创建一个结构体
class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

p = Point(1, 2)
print(p.x, p.y)

# 创建一个类
class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

p = Point(1, 2)
print(p)

# 创建一个类
class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c
