import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_object)

# 回调函数
def somefunc(x,y):
    print x,y.contents
    return x+y.contents.value

# 实例化回调函数
callback = FUNTYPE(somefunc)

# 初始化参数值
i = ctypes.c_int(2)

# 实例化回调函数

# 传入回调函数
lib.myfunc(callback,1,i)
