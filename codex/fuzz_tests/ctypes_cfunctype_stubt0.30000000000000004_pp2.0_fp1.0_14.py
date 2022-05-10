import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())

print("-"*20)

# 定义一个结构体
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

# 定义一个函数，返回结构体
@FUNTYPE
def fun():
    return POINT(1, 2)

# 调用函数，获取返回值
ret = fun()
print(ret.x, ret.y)
