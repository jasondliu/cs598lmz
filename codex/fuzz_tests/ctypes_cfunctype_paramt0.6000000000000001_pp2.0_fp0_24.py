import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(arg1, arg2):
    print("arg1 = %d, arg2 = %d" % (arg1, arg2))
    return arg1 + arg2

f = FUNTYPE(func)
print(f(1, 2))

# 创建结构体
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

p = POINT(1, 2)
print(p.x, p.y)

# 创建C类型数组
array = (ctypes.c_int * 2)(1, 2)
print(array[0], array[1])
