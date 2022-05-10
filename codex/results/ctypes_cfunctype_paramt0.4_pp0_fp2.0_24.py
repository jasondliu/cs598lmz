import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

@FUNTYPE
def myadd(a, b):
    return a + b

print myadd(1, 2)

# 通过ctypes.Structure创建结构体
class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

p = Point(1, 2)
print p.x, p.y

# 通过ctypes.Union创建联合体
class Point(ctypes.Union):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

p = Point(1, 2)
print p.x, p.y

# 通过ctypes.POINTER创建指针
p = ctypes.POINTER(Point)(Point(1, 2))
print
