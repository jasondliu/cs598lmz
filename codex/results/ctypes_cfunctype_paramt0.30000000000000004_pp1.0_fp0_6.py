import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(x):
    return x * x

f = FUNTYPE(func)
print f(2)

# 可以将回调函数作为参数传递给C函数
# 可以将回调函数作为参数传递给C函数

# 回调函数的实参
# 回调函数的实参

# 回调函数的返回值
# 回调函数的返回值

# 回调函数的实参和返回值
# 回调函数的实参和返回值

# 回调
