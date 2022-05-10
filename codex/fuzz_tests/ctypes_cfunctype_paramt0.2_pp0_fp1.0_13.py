import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    return a + b

f = FUNTYPE(func)
print(f(1, 2))

# 创建一个函数类型的实例
# 参数1：返回值类型
# 参数2：参数类型
# 参数3：参数名称
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# 创建一个函数类型的实例
f = FUNTYPE(lambda a, b: a + b)
print(f(1, 2))

# 创建一个函数类型
